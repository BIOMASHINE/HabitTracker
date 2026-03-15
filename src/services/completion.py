from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.cache import invalidate_stats_cache
from core.models import Completion, Habit


class CompletionService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_completion(
        self,
        habit_id: int,
    ):
        completion = Completion(
            habit_id=habit_id,
        )
        self.session.add(completion)

        await self.session.commit()
        await self.session.refresh(completion)

        await invalidate_stats_cache(habit_id=habit_id)
        
        return completion

    async def get_completions(self, habit_id: int):
        query = (
            select(Completion)
            .filter(Completion.habit_id == habit_id)
            .order_by(Completion.completed_at.desc())
        )

        result = await self.session.execute(query)
        completions = result.scalars().all()

        return completions

    async def remove_completion(self, completion_id: int, user):
        completion = await self.session.get(Completion, completion_id)

        if not completion:
            raise HTTPException(404, "Completion not found")

        habit = await self.session.get(Habit, completion.habit_id)

        if not habit or habit.user_id != user.id:
            raise HTTPException(404, "Completion not found")

        await self.session.delete(completion)
        await self.session.commit()
        
        await invalidate_stats_cache(habit_id=habit.id)
