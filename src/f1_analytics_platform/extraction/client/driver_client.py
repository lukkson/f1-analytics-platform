from f1_analytics_platform.extraction.http_client import BaseHttpClient
from f1_analytics_platform.extraction.mappers.driver_mapper import DriverMapper
from f1_analytics_platform.models import Driver


class DriverClient:
    def __init__(self, http_client: BaseHttpClient):
        self._http_client = http_client
        self._mapper = DriverMapper()

    def get_drivers(self, season: int) -> list[Driver]:
        response = self._http_client.get(f"/{season}/drivers.json")
        return self._mapper.map(response)
