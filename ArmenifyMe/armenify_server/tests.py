from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from ArmenifyMe.armenify_server.models import UserSettings, UserWordProgress, Word

User = get_user_model()


class ChatAnswerIdempotencyTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="u@example.com", password="secret123")
        self.client.force_authenticate(self.user)
        self.word = Word.objects.create(
            armenian="\u0562\u0561\u0580\u0587\u0587",
            translations=["hello", "hi"],
            transcription="barev",
            level="A1",
        )
        UserWordProgress.objects.create(
            user=self.user,
            word=self.word,
            status=UserWordProgress.Status.LEARNING,
        )
        UserSettings.objects.create(user=self.user, correct_threshold=2, learning_list_size=20)

    def test_same_client_message_id_is_deduplicated(self):
        payload = {
            "client_message_id": "u-1739541289000",
            "word_id": str(self.word.id),
            "answer": "hello",
        }
        first = self.client.post("/api/v1/chat/answer", data=payload, format="json")
        second = self.client.post("/api/v1/chat/answer", data=payload, format="json")

        self.assertEqual(first.status_code, status.HTTP_200_OK)
        self.assertEqual(second.status_code, status.HTTP_200_OK)
        self.assertFalse(first.data["deduplicated"])
        self.assertTrue(second.data["deduplicated"])

        progress = UserWordProgress.objects.get(user=self.user, word=self.word)
        self.assertEqual(progress.correct_count, 1)

    def test_same_client_message_id_with_other_payload_returns_conflict(self):
        first_payload = {
            "client_message_id": "u-1739541289000",
            "word_id": str(self.word.id),
            "answer": "hello",
        }
        conflict_payload = {
            "client_message_id": "u-1739541289000",
            "word_id": str(self.word.id),
            "answer": "wrong",
        }

        first = self.client.post("/api/v1/chat/answer", data=first_payload, format="json")
        conflict = self.client.post("/api/v1/chat/answer", data=conflict_payload, format="json")

        self.assertEqual(first.status_code, status.HTTP_200_OK)
        self.assertEqual(conflict.status_code, status.HTTP_409_CONFLICT)

    def test_learning_list_has_top_level_version(self):
        response = self.client.get("/api/v1/words/learning")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("list_version", response.data)
        self.assertIn("items", response.data)
