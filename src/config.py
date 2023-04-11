from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_TITLE = 'Personik'
    SERP_API_KEY: str

    class Config:
        env_file = '.env'


@lru_cache()
def get_settings():
    return Settings()
