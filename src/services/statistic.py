from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Completion


class StatsService:
    
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def count_stats(self, habit_id: int, limit: int) -> dict[str, int]:
        query = (
            select(Completion.completed_at)
            .filter(Completion.habit_id == habit_id)
            .order_by(Completion.completed_at)
            .limit(limit)
        )

        result = await self.session.execute(query)

        full_dates = result.scalars().all()

        dates = [date.date() for date in full_dates]

        streak, max_streak = 0, 0

        for i in range(len(dates) - 1):
            dates_diff = dates[i + 1] - dates[i]

            if dates_diff.days == 1:
                streak += 1

                if streak > max_streak:
                    max_streak = streak
            else:
                streak = 0

        return {
            "streak": streak,
            "max_streak": max_streak,
            "total_completions": len(dates),
        }
