import redis

def create_redis():
  return redis.ConnectionPool(
    host='redis-server',
    port=6379
  )

pool = create_redis()