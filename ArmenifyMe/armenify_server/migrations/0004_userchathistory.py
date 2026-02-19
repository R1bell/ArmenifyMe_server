from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("armenify_server", "0003_userwordprogress_manual_override"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserChatHistory",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="armenify_server.user",
                    ),
                ),
                ("messages", models.JSONField(default=list)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
