import redis
from .setting import settings

def create_redis():
  return redis.ConnectionPool(
    host=settings.redis_host,
    port=settings.redis_port
  )

pool = create_redis()