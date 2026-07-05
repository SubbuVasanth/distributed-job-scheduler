from pathlib import Path

from pydantic_settings import BaseSettings

# Resolve .env relative to this file:
# config.py -> core/ -> app/ -> backend/ -> project root
ENV_FILE = Path(__file__).resolve().parents[3] / ".env"


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = str(ENV_FILE)


settings = Settings()