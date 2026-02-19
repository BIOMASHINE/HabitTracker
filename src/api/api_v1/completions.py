from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.fastapi_users_router import current_user
from core.config import settings
from core.models import db_helper, User, Habit
from core.schemas.completion import CompletionCreate, CompletionRead
from services.completions import CompletionService

router = APIRouter(
    prefix=settings.api.v1.completions,
)


@router.post(
    "/",
    response_model=CompletionRead,
    summary="Completions: Create completion",
)
async def create_completion(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user: Annotated[User, Depends(current_user)],
    habit_id: int,
):
    habit = await session.get(Habit, habit_id)

    if not habit:
        raise HTTPException(
            status_code=404,
            detail="Habit does not exist",
        )
    if habit.user_id != user.id:
        raise HTTPException(
            status_code=403,
            detail="You are not authorized to access this Habit",
        )

    service = CompletionService(session=session)

    completion = await service.create_completion(
        habit_id=habit_id,
    )

    return completion


@router.get(
    "/",
    response_model=list[CompletionRead],
    summary="Completions: List all completions",
)
async def read_all_completions(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user: Annotated[User, Depends(current_user)],
    habit_id: int,
):
    habit = await session.get(Habit, habit_id)

    if not habit:
        raise HTTPException(
            status_code=404,
            detail="Habit does not exist",
        )

    if habit.user_id != user.id:
        raise HTTPException(
            status_code=403,
            detail="You are not authorized to access this Habit",
        )

    service = CompletionService(session=session)

    completions = await service.get_completions(habit_id=habit_id)

    return completions


@router.delete(
    "/{completion_id}",
    summary="Completions: Delete completion",
)
async def delete_completion(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user: Annotated[User, Depends(current_user)],
    completion_id: int,
) -> dict[str, bool]:
    service = CompletionService(session=session)

    await service.remove_completion(completion_id=completion_id, user=user)

    return {"success": True}
