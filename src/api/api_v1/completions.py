from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.fastapi_users_router import current_user
from api.dependencies.habits import get_user_habit
from core.config import settings
from core.models import db_helper, User
from core.schemas.completion import CompletionRead
from services.completion import CompletionService

router = APIRouter(
    prefix=settings.api.v1.completions,
)


@router.post(
    "/{habit_id}",
    response_model=CompletionRead,
    summary="Completions:Create completion",
    dependencies=[Depends(get_user_habit)],
)
async def create_completion(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    habit_id: int,
):
    service = CompletionService(session=session)

    completion = await service.create_completion(
        habit_id=habit_id,
    )

    return completion


@router.get(
    "/{habit_id}",
    response_model=list[CompletionRead],
    summary="Completions:List all completions",
    dependencies=[Depends(get_user_habit)],
)
async def read_all_completions(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    habit_id: int,
):
    service = CompletionService(session=session)

    completions = await service.get_completions(habit_id=habit_id)

    return completions


@router.delete(
    "/{completion_id}",
    summary="Completions:Delete completion",
)
async def delete_completion(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user: Annotated[User, Depends(current_user)],
    completion_id: int,
) -> dict[str, bool]:
    service = CompletionService(session=session)

    await service.remove_completion(completion_id=completion_id, user=user)

    return {"success": True}
