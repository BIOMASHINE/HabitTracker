from typing import Annotated

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.habits import get_user_habit
from core.config import settings
from core.models import db_helper
from core.schemas.stat import StatRead
from services.statistic import StatsService

router = APIRouter(
    prefix=settings.api.v1.stats,
    tags=["Stats"],
)


@router.get(
    "/habits/{habit_id}",
    summary="Stats:Count all habit's stats",
    dependencies=[Depends(get_user_habit)],
    response_model=StatRead,
)
async def stats_counter(
    habit_id: int, session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    limit: int = 30,
):
    service = StatsService(session=session)

    stats = await service.count_stats(habit_id=habit_id, limit=limit)

    return stats
