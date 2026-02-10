from django.urls import path
from analytics.views import HealthcheckView

urlpatterns = [
    path("health", HealthcheckView.as_view()),
]
