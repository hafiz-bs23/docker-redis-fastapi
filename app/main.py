from typing import Union

from fastapi import FastAPI, Depends
import redis

from .config.cache import pool

app = FastAPI()

def get_redis():
    cache = redis.Redis(connection_pool=pool)
    if cache.get("request-counter") is None:
        cache.set("request-counter", 0)
    return cache


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/check")
def read_item(cache = Depends(get_redis)):
    status = cache.ping()
    request_counter = cache.get("request-counter")
    yield {"status": status, "request_counter": request_counter}
    cache.incr("request-counter")