from f1_analytics_platform.extraction.http_client import HttpClient, BaseHttpClient
from f1_analytics_platform.extraction.mappers.lap_time_mapper import LapTimeMapper
from f1_analytics_platform.models import LapTime


class LapTimeClient:
    def __init__(self, http_client: BaseHttpClient):
        self._http_client = http_client
        self._mapper = LapTimeMapper()

    def get_laps(self, season: int, lap: int) -> list[LapTime]:
        response = self._http_client.get(f"/{season}/{lap}/laps.json")
        return self._mapper.map(response)
