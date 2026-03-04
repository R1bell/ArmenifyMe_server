from __future__ import annotations

import asyncio
from datetime import datetime

from analytics_service.celery_app import celery_app
from analytics_service.db import AsyncSessionLocal
from analytics_service.repositories import create_or_get_analytics_user, create_user_answer


async def _create_or_get_analytics_user(
    user_id: int,
    username: str = "",
    email: str = "",
) -> int:
    async with AsyncSessionLocal() as session:
        return await create_or_get_analytics_user(
            session=session,
            user_id=user_id,
            username=username,
            email=email,
        )


async def _store_user_answer(
    user_id: int,
    word: str,
    answer: str,
    is_correct: bool,
    timestamp: str,
) -> int:
    event_time = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    async with AsyncSessionLocal() as session:
        return await create_user_answer(
            session=session,
            user_id=user_id,
            word=word,
            answer=answer,
            is_correct=is_correct,
            timestamp=event_time,
        )


@celery_app.task(name="analytics.create_user")
def create_analytics_user(user_id: int, username: str = "", email: str = "") -> int:
    return asyncio.run(
        _create_or_get_analytics_user(
            user_id=user_id,
            username=username,
            email=email,
        )
    )


@celery_app.task(name="analytics.store_user_answer")
def store_user_answer(
    user_id: int,
    word: str,
    answer: str,
    is_correct: bool,
    timestamp: str,
) -> int:
    return asyncio.run(
        _store_user_answer(
            user_id=user_id,
            word=word,
            answer=answer,
            is_correct=is_correct,
            timestamp=timestamp,
        )
    )
