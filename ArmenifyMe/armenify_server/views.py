import hashlib
import json
import logging
import time

from django.db import transaction
from django.db import IntegrityError
from django.db.models import F
from django.db.models import Max
from django.utils import timezone
from django.conf import settings as django_settings
from django.core.cache import cache
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

from ArmenifyMe.armenify_server.models import (
    ChatAnswerIdempotency,
    UserChatHistory,
    UserSettings,
    UserWordProgress,
    Word,
    WordComment,
)
from ArmenifyMe.armenify_server.serializers import (
    ChatAnswerRequestSerializer,
    ChatAnswerResponseSerializer,
    ChatHistoryRequestSerializer,
    ChatHistoryResponseSerializer,
    LearnedRestoreRequestSerializer,
    LearningMoveRequestSerializer,
    LoginSerializer,
    LoginResponseSerializer,
    LogoutSerializer,
    RegisterSerializer,
    RegisterResponseSerializer,
    RefreshResponseSerializer,
    UserSettingsSerializer,
    WordCommentCreateSerializer,
    WordCommentResponseSerializer,
    WordListSerializer,
    WordProgressListSerializer,
    WordProgressSerializer,
)
from ArmenifyMe.armenify_server.tasks import add_initial_words, ensure_learning_list

logger = logging.getLogger(__name__)


def _normalize_answer(value: str) -> str:
    return value.strip().lower().replace("\u0451", "\u0435")


def _ensure_learning_size(user):
    ensure_learning_list.delay(user.id)

def _cache_key(user_id: int, list_name: str) -> str:
    return f"lists:{list_name}:user:{user_id}"


def _cache_get(key: str):
    try:
        return cache.get(key)
    except Exception as exc:
        logger.warning("cache get failed for key=%s: %s", key, exc)
        return None


def _cache_set(key: str, value, timeout: int) -> None:
    try:
        cache.set(key, value, timeout=timeout)
    except Exception as exc:
        logger.warning("cache set failed for key=%s: %s", key, exc)


def _cache_delete(key: str) -> None:
    try:
        cache.delete(key)
    except Exception as exc:
        logger.warning("cache delete failed for key=%s: %s", key, exc)


CHAT_HISTORY_MAX = 50


def _invalidate_lists(user_id: int) -> None:
    _cache_delete(_cache_key(user_id, "learning"))
    _cache_delete(_cache_key(user_id, "learned"))


def _request_hash(word_id, answer: str) -> str:
    payload = {
        "answer": _normalize_answer(answer),
        "word_id": str(word_id),
    }
    canonical = json.dumps(payload, ensure_ascii=True, sort_keys=True)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _build_list_payload(items):
    serialized_items = WordProgressSerializer(items, many=True).data
    list_version = items.aggregate(list_version=Max("progress_version"))["list_version"] or 0
    updated_at = items.aggregate(updated_at=Max("updated_at"))["updated_at"]
    return {
        "list_version": list_version,
        "updated_at": updated_at,
        "items": serialized_items,
    }


def _learning_items_queryset(user):
    return (
        UserWordProgress.objects.select_related("word")
        .filter(user=user, status=UserWordProgress.Status.LEARNING)
        .order_by("created_at")
    )


def _recalculate_statuses_sync(user, threshold: int) -> None:
    learning_qs = UserWordProgress.objects.filter(
        user=user, status=UserWordProgress.Status.LEARNING, manual_override=False
    )
    learned_qs = UserWordProgress.objects.filter(
        user=user, status=UserWordProgress.Status.LEARNED, manual_override=False
    )
    moved_to_learned = learning_qs.filter(correct_count__gte=threshold).update(
        status=UserWordProgress.Status.LEARNED,
        progress_version=F("progress_version") + 1,
    )
    moved_to_learning = learned_qs.filter(correct_count__lt=threshold).update(
        status=UserWordProgress.Status.LEARNING,
        progress_version=F("progress_version") + 1,
    )
    if moved_to_learned or moved_to_learning:
        _invalidate_lists(user.id)


class ChatAnswerView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=ChatAnswerRequestSerializer,
        responses=ChatAnswerResponseSerializer,
    )
    def post(self, request):
        started = time.monotonic()
        status_code = status.HTTP_200_OK
        deduplicated = False
        client_message_id = None

        req = ChatAnswerRequestSerializer(data=request.data)
        req.is_valid(raise_exception=True)
        client_message_id = req.validated_data["client_message_id"]
        word_id = req.validated_data["word_id"]
        answer = req.validated_data["answer"]
        req_hash = _request_hash(word_id, answer)

        existing = ChatAnswerIdempotency.objects.filter(
            user=request.user, client_message_id=client_message_id
        ).first()
        if existing:
            if existing.request_hash and existing.request_hash != req_hash:
                status_code = status.HTTP_409_CONFLICT
                return Response(
                    {
                        "error_code": "CHAT_SYNC_CONFLICT",
                        "message": "client_message_id was already used with another payload",
                    },
                    status=status_code,
                )
            deduplicated_payload = dict(existing.response_payload)
            deduplicated_payload["deduplicated"] = True
            deduplicated = True
            return Response(deduplicated_payload, status=status_code)

        try:
            with transaction.atomic():
                progress = (
                    UserWordProgress.objects.select_for_update()
                    .select_related("word")
                    .filter(user=request.user, word_id=word_id)
                    .first()
                )
                if not progress or progress.status != UserWordProgress.Status.LEARNING:
                    status_code = status.HTTP_400_BAD_REQUEST
                    return Response(
                        {"error_code": "CHAT_INVALID_WORD", "message": "word not in learning"},
                        status=status_code,
                    )

                translations = progress.word.translations or []
                normalized = _normalize_answer(answer)
                normalized_translations = [_normalize_answer(t) for t in translations]
                correct = normalized in normalized_translations

                threshold = (
                    UserSettings.objects.filter(user=request.user)
                    .values_list("correct_threshold", flat=True)
                    .first()
                )
                if threshold is None:
                    threshold = django_settings.CORRECT_THRESHOLD

                if correct:
                    progress.correct_count += 1
                    progress.progress_version += 1
                    if progress.correct_count >= threshold:
                        progress.status = UserWordProgress.Status.LEARNED
                    progress.save(update_fields=["correct_count", "progress_version", "status"])

                processed_at = timezone.now().isoformat().replace("+00:00", "Z")
                payload = {
                    "client_message_id": client_message_id,
                    "server_event_id": str(progress.id),
                    "deduplicated": False,
                    "correct": correct,
                    "correct_count": progress.correct_count,
                    "threshold": threshold,
                    "status": progress.status,
                    "expected_translations": translations,
                    "progress_version": progress.progress_version,
                    "processed_at": processed_at,
                }
                try:
                    ChatAnswerIdempotency.objects.create(
                        user=request.user,
                        client_message_id=client_message_id,
                        request_hash=req_hash,
                        response_payload=payload,
                    )
                except IntegrityError:
                    existing = ChatAnswerIdempotency.objects.select_for_update().filter(
                        user=request.user, client_message_id=client_message_id
                    ).first()
                    if existing and existing.request_hash and existing.request_hash != req_hash:
                        status_code = status.HTTP_409_CONFLICT
                        return Response(
                            {
                                "error_code": "CHAT_SYNC_CONFLICT",
                                "message": "client_message_id was already used with another payload",
                            },
                            status=status_code,
                        )
                    if existing:
                        deduplicated_payload = dict(existing.response_payload)
                        deduplicated_payload["deduplicated"] = True
                        deduplicated = True
                        return Response(deduplicated_payload, status=status_code)
                    raise

                if correct and progress.status == UserWordProgress.Status.LEARNED:
                    _invalidate_lists(request.user.id)
                    _ensure_learning_size(request.user)

                serialized = ChatAnswerResponseSerializer(payload).data
                return Response(serialized, status=status_code)
        finally:
            latency_ms = int((time.monotonic() - started) * 1000)
            logger.info(
                "chat_answer user_id=%s client_message_id=%s deduplicated=%s status_code=%s latency_ms=%s",
                request.user.id,
                client_message_id,
                deduplicated,
                status_code,
                latency_ms,
            )


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        request=RegisterSerializer,
        responses=RegisterResponseSerializer,
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        add_initial_words.delay(user.id)
        return Response({"id": user.id, "email": user.email}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        request=LoginSerializer,
        responses=LoginResponseSerializer,
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


class RefreshView(TokenRefreshView):
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        request=TokenRefreshSerializer,
        responses=RefreshResponseSerializer,
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=LogoutSerializer,
        responses=None,
    )
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = RefreshToken(serializer.validated_data["refresh"])
        token.blacklist()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LearningListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        responses=WordProgressListSerializer,
    )
    def get(self, request):
        cache_key = _cache_key(request.user.id, "learning")
        cached = _cache_get(cache_key)
        if cached is not None:
            return Response(cached)

        items = _learning_items_queryset(request.user)
        data = _build_list_payload(items)

        if not data["items"]:
            # Fallback for first login when worker is unavailable.
            ensure_learning_list(request.user.id)
            items = _learning_items_queryset(request.user)
            data = _build_list_payload(items)

        if data["items"]:
            _cache_set(cache_key, data, timeout=django_settings.CACHE_TTL)
        return Response(data)


class LearningRefillView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        responses=WordProgressListSerializer,
    )
    def post(self, request):
        ensure_learning_list(request.user.id)
        items = _learning_items_queryset(request.user)
        data = _build_list_payload(items)
        _cache_set(_cache_key(request.user.id, "learning"), data, timeout=django_settings.CACHE_TTL)
        return Response(data)


class WordListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        responses=WordListSerializer(many=True),
    )
    def get(self, request):
        words = Word.objects.order_by("created_at")
        return Response(WordListSerializer(words, many=True).data)


class LearningDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    @extend_schema(
        responses=None,
    )
    def post(self, request, word_id):
        progress = UserWordProgress.objects.filter(user=request.user, word_id=word_id).first()
        if not progress:
            return Response({"detail": "not found"}, status=status.HTTP_404_NOT_FOUND)

        progress.status = UserWordProgress.Status.DELETED
        progress.progress_version += 1
        progress.save(update_fields=["status", "progress_version"])
        _invalidate_lists(request.user.id)
        _ensure_learning_size(request.user)
        return Response({"status": "deleted"})


class LearningMoveView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    @extend_schema(
        request=LearningMoveRequestSerializer,
        responses=None,
    )
    def post(self, request, word_id):
        req = LearningMoveRequestSerializer(data=request.data)
        req.is_valid(raise_exception=True)
        manual = req.validated_data["manual"]

        progress = UserWordProgress.objects.filter(user=request.user, word_id=word_id).first()
        if not progress:
            return Response({"detail": "not found"}, status=status.HTTP_404_NOT_FOUND)

        progress.status = UserWordProgress.Status.LEARNED
        progress.manual_override = manual
        progress.progress_version += 1
        progress.save(update_fields=["status", "manual_override", "progress_version"])
        _invalidate_lists(request.user.id)
        _ensure_learning_size(request.user)
        return Response({"status": "learned", "manual": manual})


class LearnedListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        responses=WordProgressListSerializer,
    )
    def get(self, request):
        items = (
            UserWordProgress.objects.select_related("word")
            .filter(user=request.user, status=UserWordProgress.Status.LEARNED)
            .order_by("created_at")
        )
        cache_key = _cache_key(request.user.id, "learned")
        cached = _cache_get(cache_key)
        if cached is not None:
            return Response(cached)

        data = _build_list_payload(items)
        _cache_set(cache_key, data, timeout=django_settings.CACHE_TTL)
        return Response(data)


class LearnedRestoreView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    @extend_schema(
        request=LearnedRestoreRequestSerializer,
        responses=None,
    )
    def post(self, request, word_id):
        req = LearnedRestoreRequestSerializer(data=request.data)
        req.is_valid(raise_exception=True)
        reset_progress = req.validated_data["reset_progress"]

        progress = UserWordProgress.objects.filter(user=request.user, word_id=word_id).first()
        if not progress:
            return Response({"detail": "not found"}, status=status.HTTP_404_NOT_FOUND)

        progress.status = UserWordProgress.Status.LEARNING
        progress.manual_override = False
        update_fields = ["status", "manual_override", "progress_version"]
        if reset_progress:
            progress.correct_count = 0
            update_fields.append("correct_count")
        progress.progress_version += 1
        progress.save(update_fields=update_fields)
        _invalidate_lists(request.user.id)
        return Response({"status": "learning", "reset_progress": reset_progress})


class LearnedDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    @extend_schema(
        responses=None,
    )
    def post(self, request, word_id):
        progress = UserWordProgress.objects.filter(user=request.user, word_id=word_id).first()
        if not progress:
            return Response({"detail": "not found"}, status=status.HTTP_404_NOT_FOUND)

        progress.status = UserWordProgress.Status.DELETED
        progress.progress_version += 1
        progress.save(update_fields=["status", "progress_version"])
        _invalidate_lists(request.user.id)
        _ensure_learning_size(request.user)
        return Response({"status": "deleted"})


class ChatHistoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        responses=ChatHistoryResponseSerializer,
        description="Return the last up to 50 chat messages for the current user.",
    )
    def get(self, request):
        obj = UserChatHistory.objects.filter(user=request.user).first()
        messages = (obj.messages if obj else [])[-CHAT_HISTORY_MAX:]
        updated_at = obj.updated_at if obj else None
        return Response(
            ChatHistoryResponseSerializer(
                {"messages": messages, "updated_at": updated_at}
            ).data
        )

    @extend_schema(
        request=ChatHistoryRequestSerializer,
        responses=ChatHistoryResponseSerializer,
        description="Save the last 50 chat messages. Older entries are truncated.",
    )
    def put(self, request):
        ser = ChatHistoryRequestSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        messages = ser.validated_data["messages"][-CHAT_HISTORY_MAX:]
        obj, _ = UserChatHistory.objects.update_or_create(
            user=request.user,
            defaults={"messages": messages},
        )
        return Response(
            ChatHistoryResponseSerializer(
                {"messages": obj.messages, "updated_at": obj.updated_at}
            ).data
        )


class SettingsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        responses=UserSettingsSerializer,
    )
    def get(self, request):
        settings, _created = UserSettings.objects.get_or_create(
            user=request.user,
            defaults={
                "learning_list_size": django_settings.LEARNING_LIST_SIZE,
                "correct_threshold": django_settings.CORRECT_THRESHOLD,
            },
        )
        return Response(UserSettingsSerializer(settings).data)

    @transaction.atomic
    @extend_schema(
        request=UserSettingsSerializer,
        responses=UserSettingsSerializer,
    )
    def patch(self, request):
        settings, _created = UserSettings.objects.get_or_create(
            user=request.user,
            defaults={
                "learning_list_size": django_settings.LEARNING_LIST_SIZE,
                "correct_threshold": django_settings.CORRECT_THRESHOLD,
            },
        )
        serializer = UserSettingsSerializer(settings, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        _recalculate_statuses_sync(request.user, serializer.instance.correct_threshold)
        ensure_learning_list(request.user.id)
        _invalidate_lists(request.user.id)
        return Response(serializer.data)


class WordCommentCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=WordCommentCreateSerializer,
        responses=WordCommentResponseSerializer,
    )
    def post(self, request, word_id):
        serializer = WordCommentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        word = Word.objects.filter(id=word_id).first()
        if not word:
            return Response({"detail": "word not found"}, status=status.HTTP_404_NOT_FOUND)

        comment = WordComment.objects.create(
            user=request.user,
            word=word,
            text=serializer.validated_data["text"],
        )
        return Response(
            WordCommentResponseSerializer(comment).data,
            status=status.HTTP_201_CREATED,
        )
