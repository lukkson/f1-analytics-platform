from abc import abstractmethod, ABC

import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from f1_analytics_platform.config.http_config import HttpClientConfig
from f1_analytics_platform.decorators.api_decorator import handle_api_errors


class BaseHttpClient(ABC):
    @abstractmethod
    def get(self, path: str, params: dict = None) -> dict: ...


class HttpClient(BaseHttpClient):
    def __init__(self, config: HttpClientConfig):
        self._config = config
        self._session = self._build_session()

    def _build_session(self) -> requests.Session:
        session = requests.Session()

        retry_strategy = Retry(
            total=self._config.max_retries,
            backoff_factor=self._config.backoff_factor,
            status_forcelist=[429, 500, 502, 503, 504],
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("https://", adapter)

        return session

    @handle_api_errors
    def get(self, path: str, params: dict = None) -> dict:
        url = f"{self._config.base_url}{path}"
        response = self._session.get(url, params=params, timeout=self._config.timeout)
        response.raise_for_status()
        return response.json()

    def close(self) -> None:
        self._session.close()
