from django.db import models


class AnalyticsUser(models.Model):
    user_id = models.BigIntegerField(unique=True)
    username = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
