from celery import shared_task

from analytics.models import AnalyticsUser


@shared_task(name="analytics.create_user")
def create_analytics_user(user_id: int, username: str = "", email: str = "") -> int:
    if user_id is None:
        return 0

    obj, _created = AnalyticsUser.objects.get_or_create(
        user_id=user_id,
        defaults={"username": username, "email": email},
    )
    return obj.id
