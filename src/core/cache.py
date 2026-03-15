import logging

import json
from typing import Any

from core.redis_client import get_redis


logger = logging.getLogger(__name__)


async def cache_get(key: str) -> Any | None:
    r = await get_redis()
    data = await r.get(key)
    
    if data:
        return json.loads(data)
    return None

async def cache_set(key: str, value: Any, ttl: int = 300):
    r = await get_redis()
    
    await r.setex(key, ttl, json.dumps(value))

async def invalidate_stats_cache(habit_id: int):
    r = await get_redis()
    keys = await r.keys(f"stats:habit:{habit_id}:limit:*")
    
    if keys:
        await r.delete(*keys)
        logger.debug(f"Invalidated {len(keys)} cache keys for habit {habit_id}")
