import logging

from core.config import settings
from typing import Optional

import redis.asyncio as redis

logger = logging.getLogger(__name__)

_redis_client: Optional[redis.Redis] = None

async def get_redis() -> redis.Redis:
    global _redis_client
    
    if _redis_client is None:
        redis_url = settings.redis.url
        try:
            _redis_client = await redis.from_url(redis_url, decode_responses=True)
            await _redis_client.ping() # type: ignore
            logger.info("Connected to Redis")
        except Exception as e:
            logger.error(f"Failed to connect to Redis: {e}")
            raise
    return _redis_client

async def close_redis():
    global _redis_client
    
    if _redis_client:
        await _redis_client.aclose()
        _redis_client = None
        logger.info("Redis connection closed")

