import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseSettings):
    duck_db_path: str

    model_config = SettingsConfigDict(
        env_prefix="F1_", env_file=f".env.{os.getenv('ENV', 'prod')}", extra="ignore"
    )
