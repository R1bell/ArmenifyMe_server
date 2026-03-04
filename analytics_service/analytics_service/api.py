from __future__ import annotations

from fastapi import APIRouter, Depends, Query

from analytics_service.db import get_session
from analytics_service.repositories import (
    get_all_analytics_users,
    get_user_answers_by_user_id,
)
from analytics_service.schemas import AnalyticsUserResponse, UserAnswerResponse

router = APIRouter()


@router.get("/health")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/users", response_model=list[AnalyticsUserResponse])
async def list_users(session=Depends(get_session)) -> list[AnalyticsUserResponse]:
    users = await get_all_analytics_users(session)
    return [
        AnalyticsUserResponse(
            id=user.id,
            user_id=user.user_id,
            username=user.username,
            email=user.email,
            created_at=user.created_at,
        )
        for user in users
    ]


@router.get("/users/answers", response_model=list[UserAnswerResponse])
async def list_user_answers(
    user_id: int = Query(..., description="Analytics user identifier"),
    session=Depends(get_session),
) -> list[UserAnswerResponse]:
    answers = await get_user_answers_by_user_id(session=session, user_id=user_id)
    return [
        UserAnswerResponse(
            id=answer.id,
            user_id=answer.user_id,
            word=answer.word,
            answer=answer.answer,
            is_correct=answer.is_correct,
            timestamp=answer.timestamp,
        )
        for answer in answers
    ]
