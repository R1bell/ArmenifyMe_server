from celery import shared_task
from django.conf import settings as django_settings
from django.core.cache import cache

from ArmenifyMe.armenify_server.models import User, UserSettings, UserWordProgress, Word


def _invalidate_lists(user_id: int) -> None:
    cache.delete(f"lists:learning:user:{user_id}")
    cache.delete(f"lists:learned:user:{user_id}")


@shared_task
def add_initial_words(user_id: int) -> int:
    user = User.objects.filter(id=user_id).first()
    if not user:
        return 0

    settings, _created = UserSettings.objects.get_or_create(
        user=user,
        defaults={
            "learning_list_size": django_settings.LEARNING_LIST_SIZE,
            "correct_threshold": django_settings.CORRECT_THRESHOLD,
        },
    )
    target_size = settings.learning_list_size

    existing_word_ids = UserWordProgress.objects.filter(user=user).values_list(
        "word_id", flat=True
    )
    word_ids = list(
        Word.objects.exclude(id__in=existing_word_ids)
        .order_by("?")
        .values_list("id", flat=True)[:target_size]
    )
    if not word_ids:
        return 0

    created = UserWordProgress.objects.bulk_create(
        [
            UserWordProgress(
                user=user,
                word_id=word_id,
                status=UserWordProgress.Status.LEARNING,
            )
            for word_id in word_ids
        ]
    )
    _invalidate_lists(user.id)
    return len(created)


@shared_task
def ensure_learning_list(user_id: int) -> int:
    user = User.objects.filter(id=user_id).first()
    if not user:
        return 0

    settings, _created = UserSettings.objects.get_or_create(
        user=user,
        defaults={
            "learning_list_size": django_settings.LEARNING_LIST_SIZE,
            "correct_threshold": django_settings.CORRECT_THRESHOLD,
        },
    )
    target_size = settings.learning_list_size
    current_count = UserWordProgress.objects.filter(
        user=user, status=UserWordProgress.Status.LEARNING
    ).count()
    if current_count >= target_size:
        return 0

    needed = target_size - current_count
    existing_word_ids = UserWordProgress.objects.filter(user=user).values_list(
        "word_id", flat=True
    )
    word_ids = list(
        Word.objects.exclude(id__in=existing_word_ids)
        .order_by("?")
        .values_list("id", flat=True)[:needed]
    )
    if not word_ids:
        return 0

    created = UserWordProgress.objects.bulk_create(
        [
            UserWordProgress(
                user=user,
                word_id=word_id,
                status=UserWordProgress.Status.LEARNING,
            )
            for word_id in word_ids
        ]
    )
    _invalidate_lists(user.id)
    return len(created)
