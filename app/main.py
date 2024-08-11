from typing import Union

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import redis

from .config.cache import pool
from .config.setting import settings
from .config.db import init_db, get_session

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_redis():
    cache = redis.Redis(connection_pool=pool)
    if cache.get("request-counter") is None:
        cache.set("request-counter", 0)
    return cache


@app.get("/")
def read_root():
    return {"data": "Hello World"}

@app.get("/ping")
def ping():
    return {"status": "healthy"}

@app.get("/set/{key}/{value}")
def read_item(key: str, value: Union[str, int], cache = Depends(get_redis)):
    cache.set(key, value)
    return {key: value}

@app.get("/show/{key}")
def read_item(key: str, cache = Depends(get_redis)):
    value = cache.get(key)
    return {key: value}

@app.get("/check")
def read_item(cache = Depends(get_redis)):
    status = cache.ping()
    request_counter = cache.get("request-counter")
    yield {"status": status, "request_counter": request_counter}
    cache.incr("request-counter")