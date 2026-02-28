from typing import TYPE_CHECKING, Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Habit
from core.schemas.habit import HabitUpdate, HabitCreate

if TYPE_CHECKING:
    from api.api_v1.habits import UserDep


class HabitService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_habits(
        self,
        user: "UserDep",
    ) -> Sequence[Habit]:
        query = (
            select(Habit)
            .filter(Habit.user_id == user.id)
            .order_by(Habit.id)
        )

        result = await self.session.execute(query)

        return result.scalars().all()

    async def create_habit(
        self,
        user: "UserDep",
        habit_create: HabitCreate,
    ) -> Habit:
        habit = Habit(
            user_id=user.id,
            title=habit_create.title,
            description=habit_create.description,
            is_active=habit_create.is_active,
        )

        self.session.add(habit)

        await self.session.commit()
        await self.session.refresh(habit)

        return habit

    async def update_habit(
        self,
        habit: Habit,
        habit_update: HabitUpdate,
    ) -> Habit:
        update_data = habit_update.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(habit, field, value)

        self.session.add(habit)

        await self.session.commit()
        await self.session.refresh(habit)

        return habit

    async def delete_habit(
        self,
        habit: Habit,
    ):
        await self.session.delete(habit)
        await self.session.commit()
