from __future__ import annotations

from datetime import datetime

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from analytics_service.models import AnalyticsUser, UserAnswer


async def get_all_analytics_users(session: AsyncSession) -> list[AnalyticsUser]:
    """Return all analytics users ordered by creation time."""
    result = await session.scalars(
        select(AnalyticsUser).order_by(AnalyticsUser.created_at.asc())
    )
    return list(result.all())


async def create_or_get_analytics_user(
    session: AsyncSession,
    user_id: int,
    username: str = "",
    email: str = "",
) -> int:
    """Create an analytics user if it does not exist and return its primary key.

    The function attempts to insert a new row into the analytics users table
    using the provided user data. If a row with the same ``user_id`` already
    exists, no new row is created and the existing record id is returned.

    :param session: Async SQLAlchemy session used to execute database operations.
    :param user_id: External user identifier stored as a unique key in analytics.
    :param username: Username to persist for a newly created analytics user.
    :param email: Email to persist for a newly created analytics user.
    :returns: The primary key of the created or existing analytics user. Returns
        ``0`` if ``user_id`` is ``None``.
    :rtype: int
    """
    if user_id is None:
        return 0

    result = await session.execute(
        insert(AnalyticsUser)
        .values(user_id=user_id, username=username, email=email)
        .on_conflict_do_nothing(index_elements=[AnalyticsUser.user_id])
        .returning(AnalyticsUser.id)
    )
    created_id = result.scalar_one_or_none()
    if created_id is not None:
        await session.commit()
        return int(created_id)

    existing_id = await session.scalar(
        select(AnalyticsUser.id).where(AnalyticsUser.user_id == user_id)
    )
    await session.commit()
    return int(existing_id) if existing_id is not None else 0


async def get_user_answers_by_user_id(
    session: AsyncSession,
    user_id: int,
) -> list[UserAnswer]:
    """Return all stored answer events for the given analytics user id."""
    result = await session.scalars(
        select(UserAnswer)
        .where(UserAnswer.user_id == user_id)
        .order_by(UserAnswer.timestamp.desc(), UserAnswer.id.desc())
    )
    return list(result.all())


async def create_user_answer(
    session: AsyncSession,
    user_id: int,
    word: str,
    answer: str,
    is_correct: bool,
    timestamp: datetime,
) -> int:
    """Persist a user answer event in the analytics database.

    :param session: Async SQLAlchemy session used to execute database operations.
    :param user_id: External user identifier associated with the answer event.
    :param word: Word shown to the user when the answer was submitted.
    :param answer: Raw answer submitted by the user.
    :param is_correct: Flag indicating whether the answer was correct.
    :param timestamp: Timestamp when the answer was processed by the backend.
    :returns: Primary key of the created analytics answer row.
    :rtype: int
    """
    result = await session.execute(
        insert(UserAnswer)
        .values(
            user_id=user_id,
            word=word,
            answer=answer,
            is_correct=is_correct,
            timestamp=timestamp,
        )
        .returning(UserAnswer.id)
    )
    await session.commit()
    return int(result.scalar_one())
