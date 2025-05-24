from enum import StrEnum
from typing import Any

from pydantic_settings import BaseSettings


class AppEnv(StrEnum):
    DEV = "dev"
    PROD = "prod"


class Settings(BaseSettings, extra="allow"):
    admin_auth_key: str

    app_env: AppEnv

    public_key: str
    jwt_algorithm: str

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)


settings = Settings(_env_file=".env", _env_file_encoding="utf-8")
