import uuid

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Word(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    armenian = models.TextField(unique=True)
    translations = models.JSONField()
    transcription = models.TextField()
    level = models.TextField(default="A1")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserWordProgress(models.Model):
    class Status(models.TextChoices):
        LEARNING = "learning", "learning"
        LEARNED = "learned", "learned"
        DELETED = "deleted", "deleted"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    status = models.CharField(max_length=16, choices=Status.choices)
    correct_count = models.IntegerField(default=0)
    last_asked_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "word"], name="uq_user_word"),
        ]
        indexes = [
            models.Index(fields=["user", "status", "last_asked_at"], name="idx_user_status_last"),
        ]


class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    correct_threshold = models.IntegerField(default=10)
    learning_list_size = models.IntegerField(default=20)
    updated_at = models.DateTimeField(auto_now=True)


class ChatMessage(models.Model):
    class Role(models.TextChoices):
        USER = "user", "user"
        SYSTEM = "system", "system"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=16, choices=Role.choices)
    word = models.ForeignKey(Word, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
