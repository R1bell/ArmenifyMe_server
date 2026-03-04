from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class AnalyticsUserResponse(BaseModel):
    id: int
    user_id: int
    username: str
    email: str
    created_at: datetime


class UserAnswerResponse(BaseModel):
    id: int
    user_id: int
    word: str
    answer: str
    is_correct: bool
    timestamp: datetime
