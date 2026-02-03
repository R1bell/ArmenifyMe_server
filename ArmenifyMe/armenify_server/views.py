from django.db import transaction
from django.db.models import F
from django.utils import timezone
from django.conf import settings as django_settings
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

from ArmenifyMe.armenify_server.models import UserSettings, UserWordProgress, Word
from ArmenifyMe.armenify_server.serializers import (
    ChatAnswerRequestSerializer,
    ChatAnswerResponseSerializer,
    ChatQuestionSerializer,
    LoginSerializer,
    LoginResponseSerializer,
    RegisterSerializer,
    RegisterResponseSerializer,
    LogoutSerializer,
    RefreshResponseSerializer,
    UserSettingsSerializer,
    WordProgressSerializer,
)
from ArmenifyMe.armenify_server.tasks import add_initial_words, ensure_learning_list


def _normalize_answer(value: str) -> str:
    return value.strip().lower().replace("ё", "е")


def _ensure_learning_size(user):
    ensure_learning_list.delay(user.id)


class ChatQuestionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        responses=ChatQuestionSerializer,
    )
    def get(self, request):
        progress = (
            UserWordProgress.objects.select_related("word")
            .filter(user=request.user, status=UserWordProgress.Status.LEARNING)
            .order_by(F("last_asked_at").asc(nulls_first=True))
            .first()
        )
        if not progress:
            return Response({"detail": "no learning words"}, status=status.HTTP_404_NOT_FOUND)

        progress.last_asked_at = timezone.now()
        progress.save(update_fields=["last_asked_at"])

        payload = {
            "word_id": progress.word.id,
            "armenian": progress.word.armenian,
            "transcription": progress.word.transcription,
        }
        return Response(ChatQuestionSerializer(payload).data)


class ChatAnswerView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=ChatAnswerRequestSerializer,
        responses=ChatAnswerResponseSerializer,
    )
    @transaction.atomic
    def post(self, request):
        req = ChatAnswerRequestSerializer(data=request.data)
        req.is_valid(raise_exception=True)
        word_id = req.validated_data["word_id"]
        answer = req.validated_data["answer"]

        progress = UserWordProgress.objects.select_related("word").filter(
            user=request.user, word_id=word_id
        ).first()
        if not progress or progress.status != UserWordProgress.Status.LEARNING:
            return Response({"detail": "word not in learning"}, status=status.HTTP_400_BAD_REQUEST)

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
            progress.correct_count = F("correct_count") + 1
            progress.save(update_fields=["correct_count"])
            progress.refresh_from_db(fields=["correct_count"])
            if progress.correct_count >= threshold:
                progress.status = UserWordProgress.Status.LEARNED
                progress.save(update_fields=["status"])
                _ensure_learning_size(request.user)

        payload = {
            "correct": correct,
            "correct_count": progress.correct_count,
            "threshold": threshold,
            "status": progress.status,
            "expected_translations": translations,
        }
        return Response(ChatAnswerResponseSerializer(payload).data)


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
        responses=WordProgressSerializer(many=True),
    )
    def get(self, request):
        items = (
            UserWordProgress.objects.select_related("word")
            .filter(user=request.user, status=UserWordProgress.Status.LEARNING)
            .order_by("created_at")
        )
        return Response(WordProgressSerializer(items, many=True).data)


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
        progress.save(update_fields=["status"])
        _ensure_learning_size(request.user)
        return Response({"status": "deleted"})


class LearningMoveView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    @extend_schema(
        responses=None,
    )
    def post(self, request, word_id):
        progress = UserWordProgress.objects.filter(user=request.user, word_id=word_id).first()
        if not progress:
            return Response({"detail": "not found"}, status=status.HTTP_404_NOT_FOUND)

        progress.status = UserWordProgress.Status.LEARNED
        progress.save(update_fields=["status"])
        _ensure_learning_size(request.user)
        return Response({"status": "learned"})


class LearnedListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        responses=WordProgressSerializer(many=True),
    )
    def get(self, request):
        items = (
            UserWordProgress.objects.select_related("word")
            .filter(user=request.user, status=UserWordProgress.Status.LEARNED)
            .order_by("created_at")
        )
        return Response(WordProgressSerializer(items, many=True).data)


class LearnedRestoreView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    @extend_schema(
        responses=None,
    )
    def post(self, request, word_id):
        progress = UserWordProgress.objects.filter(user=request.user, word_id=word_id).first()
        if not progress:
            return Response({"detail": "not found"}, status=status.HTTP_404_NOT_FOUND)

        progress.status = UserWordProgress.Status.LEARNING
        progress.save(update_fields=["status"])
        return Response({"status": "learning"})


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
        progress.save(update_fields=["status"])
        _ensure_learning_size(request.user)
        return Response({"status": "deleted"})


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
        settings, _created = UserSettings.objects.get_or_create(user=request.user)
        serializer = UserSettingsSerializer(settings, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
