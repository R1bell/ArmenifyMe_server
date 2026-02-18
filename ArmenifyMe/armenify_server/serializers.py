from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ArmenifyMe.armenify_server.models import UserSettings, UserWordProgress

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class ChatQuestionSerializer(serializers.Serializer):
    word_id = serializers.UUIDField()
    armenian = serializers.CharField()
    transcription = serializers.CharField()


class ChatAnswerRequestSerializer(serializers.Serializer):
    client_message_id = serializers.CharField(max_length=128)
    word_id = serializers.UUIDField()
    answer = serializers.CharField()


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

    class Meta:
        model = UserWordProgress
        fields = ["word_id", "armenian", "transcription", "translations", "correct_count"]


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
