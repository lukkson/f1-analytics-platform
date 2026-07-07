import os
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class HttpClientConfig(BaseSettings):
    base_url: str
    timeout: int = 10
    max_retries: int = 3
    backoff_factor: int = 1
    api_key: Optional[str] = None

    model_config = SettingsConfigDict(
        env_prefix="F1_", env_file=f".env.{os.getenv('ENV', 'prod')}", extra="ignore"
    )
