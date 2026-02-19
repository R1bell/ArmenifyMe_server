from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from ArmenifyMe.armenify_server.models import UserSettings, UserWordProgress, Word, WordComment

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


class WordCommentTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="commenter@example.com", password="secret123")
        self.word = Word.objects.create(
            armenian="\u0562\u0561\u0580\u0587\u0587",
            translations=["hello", "hi"],
            transcription="barev",
            level="A1",
        )

    def test_create_word_comment(self):
        self.client.force_authenticate(self.user)
        payload = {"text": "Перевод не совсем корректный в этом контексте"}

        response = self.client.post(f"/api/v1/words/{self.word.id}/comment", data=payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["word_id"], str(self.word.id))
        self.assertEqual(response.data["text"], payload["text"])
        self.assertEqual(WordComment.objects.filter(user=self.user, word=self.word).count(), 1)


class WordListTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="words@example.com", password="secret123")
        self.word1 = Word.objects.create(
            armenian="\u0562\u0561\u0580\u0587\u0587",
            translations=["hello"],
            transcription="barev",
            level="A1",
        )
        self.word2 = Word.objects.create(
            armenian="\u0577\u0576\u0578\u0580\u0570\u0561\u056f\u0561\u056c",
            translations=["thanks"],
            transcription="shnorhakal",
            level="A1",
        )

    def test_list_all_words(self):
        self.client.force_authenticate(self.user)
        response = self.client.get("/api/v1/words")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)
        self.assertIn("id", response.data[0])
        self.assertIn("armenian", response.data[0])
        self.assertIn("translations", response.data[0])
