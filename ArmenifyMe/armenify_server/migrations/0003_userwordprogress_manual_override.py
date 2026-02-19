from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("armenify_server", "0002_chat_answer_idempotency_and_progress_version"),
    ]

    operations = [
        migrations.AddField(
            model_name="userwordprogress",
            name="manual_override",
            field=models.BooleanField(default=False),
        ),
    ]

