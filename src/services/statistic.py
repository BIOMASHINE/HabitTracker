from datetime import date
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Completion
from core.cache import cache_get, cache_set

class StatsService:
    
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def count_stats(self, habit_id: int, limit: int) -> dict[str, int | list[date]]:
        cache_key = f"stats:habit:{habit_id}:limit:{limit}"

        cached_result = await cache_get(cache_key)
        if cached_result is not None:
            return cached_result

        if limit == -1:
            query = (
                select(Completion.completed_at)
                .filter(Completion.habit_id == habit_id)
                .order_by(Completion.completed_at)
            )
        else:
            query = (
                select(Completion.completed_at)
                .filter(Completion.habit_id == habit_id)
                .order_by(Completion.completed_at)
                .limit(limit)
            )

        result = await self.session.execute(query)
        full_dates = result.scalars().all()
        dates = [d.date() for d in full_dates]

        streak, max_streak = 0, 0
        for i in range(len(dates) - 1):
            diff = dates[i + 1] - dates[i]
            if diff.days == 1:
                streak += 1
                if streak > max_streak:
                    max_streak = streak
            else:
                streak = 0

        result_data = {
            "streak": streak,
            "max_streak": max_streak,
            "total_completions": len(dates),
            "dates": [d.isoformat() for d in dates]
        }

        await cache_set(cache_key, result_data, ttl=300)

        return result_data
