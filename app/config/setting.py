from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    redis_host: str = os.getenv("REDIS_HOST", "localhost")
    redis_port: int = os.getenv("REDIS_PORT", 6379)
    postgres_host: str = os.getenv("POSTGRES_HOST", "localhost")
    postgres_port: int = os.getenv("POSTGRES_PORT", 5432)
    postgres_user: str = os.getenv("POSTGRES_USER", "postgres")
    postgres_password: str = os.getenv("POSTGRES_PASSWORD", "postgres")
    postgres_db: str = os.getenv("POSTGRES_DB", "postgres")
    origins: list = ["http://localhost", "http://localhost:8080"]


settings = Settings()