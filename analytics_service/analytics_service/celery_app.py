from celery import Celery

from analytics_service.config import settings

celery_app = Celery("analytics_service")
celery_app.conf.update(
    broker_url=settings.celery_broker_url,
    result_expires=settings.celery_result_expires,
    accept_content=["json"],
    task_serializer="json",
    task_ignore_result=settings.celery_task_ignore_result,
    worker_prefetch_multiplier=settings.celery_worker_prefetch_multiplier,
    task_default_queue=settings.celery_task_default_queue,
    task_routes={
        "analytics.create_user": {
            "queue": settings.celery_analytics_queue,
        },
        "analytics.store_user_answer": {
            "queue": settings.celery_analytics_queue,
        }
    },
)
celery_app.autodiscover_tasks(["analytics_service"])
