from typing import Annotated

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.fastapi_users_router import current_user
from core.config import settings
from core.models import User, db_helper, Habit
from core.schemas.habit import HabitRead, HabitCreate, HabitUpdate

from services.habit import HabitService

from api.dependencies.habits import get_user_habit

from api.api_v1.completions import router as completion_router
from .stats import router as stat_router

router = APIRouter(
    prefix=settings.api.v1.habits,
    tags=["Habits"],
)
router.include_router(completion_router)
router.include_router(stat_router)

UserDep = Annotated[
    User,
    Depends(current_user),
]
SessionDep = Annotated[
    AsyncSession,
    Depends(db_helper.session_getter),
]


@router.get(
    "",
    response_model=list[HabitRead],
    summary="Habits:Get Habits",
)
async def get_habits(
    user: UserDep,
    session: SessionDep,
):
    service = HabitService(session=session)

    habits = await service.get_habits(user=user)

    return habits


@router.get(
    "/{habit_id}",
    response_model=HabitRead,
    summary="Habits:Get Habit",
)
async def get_habit(
    habit: Annotated[int, Depends(get_user_habit)],
):
    return habit


@router.post(
    "",
    response_model=HabitRead,
    summary="Habits:Create Habit",
)
async def create_habit(
    user: UserDep,
    session: SessionDep,
    habit_data: HabitCreate,
):
    service = HabitService(session=session)

    habit = await service.create_habit(
        user=user,
        habit_create=habit_data,
    )

    return habit


@router.patch(
    "/{habit_id}",
    response_model=HabitRead,
    summary="Habits:Update Habit",
)
async def update_habit(
    habit_update: HabitUpdate,
    session: SessionDep,
    habit: Annotated[Habit, Depends(get_user_habit)],
):
    service = HabitService(session=session)

    return await service.update_habit(habit=habit, habit_update=habit_update)


@router.delete(
    "/{habit_id}",
    summary="Habits:Delete Habit",
)
async def delete_habit(
    session: SessionDep,
    habit: Annotated[Habit, Depends(get_user_habit)],
) -> dict[str, bool]:
    service = HabitService(session=session)

    await service.delete_habit(habit=habit)

    return {"success": True}
