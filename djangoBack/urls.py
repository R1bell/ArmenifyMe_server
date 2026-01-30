"""
URL configuration for djangoBack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from djangoBack.armenify_server import views

urlpatterns = [
    path("api/v1/auth/register", views.RegisterView.as_view()),
    path("api/v1/auth/login", views.LoginView.as_view()),
    path("api/v1/auth/refresh", views.RefreshView.as_view()),
    path("api/v1/auth/logout", views.LogoutView.as_view()),
    path("api/v1/chat/question", views.ChatQuestionView.as_view()),
    path("api/v1/chat/answer", views.ChatAnswerView.as_view()),
    path("api/v1/words/learning", views.LearningListView.as_view()),
    path("api/v1/words/learning/<uuid:word_id>/delete", views.LearningDeleteView.as_view()),
    path("api/v1/words/learning/<uuid:word_id>/move", views.LearningMoveView.as_view()),
    path("api/v1/words/learned", views.LearnedListView.as_view()),
    path("api/v1/words/learned/<uuid:word_id>/restore", views.LearnedRestoreView.as_view()),
    path("api/v1/words/learned/<uuid:word_id>/delete", views.LearnedDeleteView.as_view()),
    path("api/v1/settings", views.SettingsView.as_view()),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

