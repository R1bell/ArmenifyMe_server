import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("armenify_server", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userwordprogress",
            name="progress_version",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name="ChatAnswerIdempotency",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("client_message_id", models.CharField(max_length=128)),
                ("request_hash", models.CharField(blank=True, max_length=64, null=True)),
                ("response_payload", models.JSONField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="chatansweridempotency",
            constraint=models.UniqueConstraint(
                fields=("user", "client_message_id"),
                name="uq_chat_answer_idempotency_user_client_message",
            ),
        ),
    ]
