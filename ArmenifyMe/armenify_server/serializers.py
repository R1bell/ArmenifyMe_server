from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ArmenifyMe.armenify_server.models import UserSettings, UserWordProgress, Word, WordComment

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class ChatAnswerRequestSerializer(serializers.Serializer):
    client_message_id = serializers.CharField(max_length=128)
    word_id = serializers.UUIDField()
    answer = serializers.CharField()


class LearningMoveRequestSerializer(serializers.Serializer):
    manual = serializers.BooleanField(required=False, default=False)


class LearnedRestoreRequestSerializer(serializers.Serializer):
    reset_progress = serializers.BooleanField(required=False, default=False)


class ChatAnswerResponseSerializer(serializers.Serializer):
    client_message_id = serializers.CharField()
    server_event_id = serializers.UUIDField()
    deduplicated = serializers.BooleanField()
    correct = serializers.BooleanField()
    correct_count = serializers.IntegerField()
    threshold = serializers.IntegerField()
    status = serializers.CharField()
    expected_translations = serializers.ListField(child=serializers.CharField())
    progress_version = serializers.IntegerField()
    processed_at = serializers.DateTimeField()


class WordProgressSerializer(serializers.ModelSerializer):
    word_id = serializers.UUIDField(source="word.id", read_only=True)
    armenian = serializers.CharField(source="word.armenian", read_only=True)
    transcription = serializers.CharField(source="word.transcription", read_only=True)
    translations = serializers.JSONField(source="word.translations", read_only=True)
    manual = serializers.BooleanField(source="manual_override", read_only=True)

    class Meta:
        model = UserWordProgress
        fields = [
            "word_id",
            "armenian",
            "transcription",
            "translations",
            "correct_count",
            "manual",
        ]


class WordListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ["id", "armenian", "translations", "transcription", "level"]


class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = ["correct_threshold", "learning_list_size"]


class WordProgressListSerializer(serializers.Serializer):
    list_version = serializers.IntegerField()
    updated_at = serializers.DateTimeField(allow_null=True)
    items = WordProgressSerializer(many=True)


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=6)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("email already exists")
        return value

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        user = User.objects.create_user(
            email=email,
            password=password,
        )
        return user


class LoginSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD


class LoginResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()


class RegisterResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    email = serializers.EmailField()


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class RefreshResponseSerializer(serializers.Serializer):
    access = serializers.CharField()


class ChatHistoryMessageSerializer(serializers.Serializer):
    id = serializers.CharField(required=False, allow_blank=True)
    role = serializers.ChoiceField(choices=["receiver", "sender"])
    text = serializers.CharField()
    meta = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    correct = serializers.BooleanField(required=False, allow_null=True)
    badge = serializers.DictField(required=False, allow_null=True)
    wordId = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    armenian = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    translations = serializers.ListField(
        child=serializers.CharField(), required=False, allow_null=True
    )
    clientMessageId = serializers.CharField(
        required=False, allow_blank=True, allow_null=True
    )
    syncStatus = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    syncAttempts = serializers.IntegerField(required=False, allow_null=True)
    syncError = serializers.CharField(required=False, allow_blank=True, allow_null=True)


class ChatHistoryResponseSerializer(serializers.Serializer):
    messages = serializers.ListField(child=serializers.DictField(), allow_empty=True)
    updated_at = serializers.DateTimeField(allow_null=True)


class ChatHistoryRequestSerializer(serializers.Serializer):
    messages = ChatHistoryMessageSerializer(many=True)


class WordCommentCreateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=2000)

    def validate_text(self, value):
        text = value.strip()
        if not text:
            raise serializers.ValidationError("comment text cannot be empty")
        return text


class WordCommentResponseSerializer(serializers.ModelSerializer):
    word_id = serializers.UUIDField(source="word.id", read_only=True)

    class Meta:
        model = WordComment
        fields = ["id", "word_id", "text", "created_at"]
