from f1_analytics_platform.extraction.http_client import HttpClient, BaseHttpClient
from f1_analytics_platform.extraction.mappers.pit_stop_mapper import PitStopMapper
from f1_analytics_platform.models import PitStop


class PitStopClient:
    def __init__(self, http_client: BaseHttpClient):
        self._http_client = http_client
        self._mapper = PitStopMapper()

    def get_pit_stops(self, season: int, lap: int) -> list[PitStop]:
        response = self._http_client.get(f"/{season}/{lap}/pitstops.json")
        return self._mapper.map(response)
