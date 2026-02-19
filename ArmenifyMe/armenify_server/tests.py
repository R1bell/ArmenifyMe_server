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


class ManualProgressFlowTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="manual@example.com", password="secret123")
        self.client.force_authenticate(self.user)
        self.word = Word.objects.create(
            armenian="\u056f\u0561\u057f",
            translations=["cat"],
            transcription="kat",
            level="A1",
        )
        UserSettings.objects.create(user=self.user, correct_threshold=5, learning_list_size=20)
        self.progress = UserWordProgress.objects.create(
            user=self.user,
            word=self.word,
            status=UserWordProgress.Status.LEARNING,
            correct_count=3,
        )

    def test_manual_move_marks_word_as_manual_and_exposes_flag_in_learned_list(self):
        move_response = self.client.post(
            f"/api/v1/words/learning/{self.word.id}/move",
            data={"manual": True},
            format="json",
        )
        self.assertEqual(move_response.status_code, status.HTTP_200_OK)
        self.assertTrue(move_response.data["manual"])

        self.progress.refresh_from_db()
        self.assertEqual(self.progress.status, UserWordProgress.Status.LEARNED)
        self.assertTrue(self.progress.manual_override)

        learned_response = self.client.get("/api/v1/words/learned")
        self.assertEqual(learned_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(learned_response.data["items"]), 1)
        self.assertTrue(learned_response.data["items"][0]["manual"])

    def test_restore_with_reset_progress_resets_counter_and_clears_manual_override(self):
        self.progress.status = UserWordProgress.Status.LEARNED
        self.progress.correct_count = 5
        self.progress.manual_override = True
        self.progress.save(update_fields=["status", "correct_count", "manual_override"])

        restore_response = self.client.post(
            f"/api/v1/words/learned/{self.word.id}/restore",
            data={"reset_progress": True},
            format="json",
        )
        self.assertEqual(restore_response.status_code, status.HTTP_200_OK)
        self.assertTrue(restore_response.data["reset_progress"])

        self.progress.refresh_from_db()
        self.assertEqual(self.progress.status, UserWordProgress.Status.LEARNING)
        self.assertEqual(self.progress.correct_count, 0)
        self.assertFalse(self.progress.manual_override)

    def test_settings_recalculate_keeps_manual_learned_words_in_learned(self):
        self.progress.status = UserWordProgress.Status.LEARNED
        self.progress.correct_count = 1
        self.progress.manual_override = True
        self.progress.save(update_fields=["status", "correct_count", "manual_override"])

        response = self.client.patch(
            "/api/v1/settings",
            data={"correct_threshold": 5},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.progress.refresh_from_db()
        self.assertEqual(self.progress.status, UserWordProgress.Status.LEARNED)
        self.assertTrue(self.progress.manual_override)
