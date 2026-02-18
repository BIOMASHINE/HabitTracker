from typing import Annotated, Type

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.fastapi_users_router import current_user
from core.models import User, db_helper, Habit


async def get_user_habit(
    habit_id: int,
    user: Annotated[User, Depends(current_user)],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> Type[Habit]:
    habit = await session.get(Habit, habit_id)

    if not habit:
        raise HTTPException(
            status_code=404,
            detail="Habit does not exist",
        )

    if user.id != habit.user_id:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to perform this action",
        )

    return habit
