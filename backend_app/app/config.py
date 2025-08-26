from pydantic_settings import BaseSettings
from functools import lru_cache


class AppConfig(BaseSettings):
    mongo_url: str = "mongodb://mongo:27017"
    mongo_db: str = "task_management_assignment_db"
    jwt_secret: str = "your_secret_key"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    allowed_hosts: list[str] = ["127.0.0.1", "localhost"]
    cors_origins: list[str] = [
        "http://localhost:5173",
    ]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_config():
    return AppConfig()
