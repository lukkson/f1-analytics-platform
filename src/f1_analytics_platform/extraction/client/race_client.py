from f1_analytics_platform.extraction.http_client import HttpClient, BaseHttpClient
from f1_analytics_platform.extraction.mappers.race_mapper import RaceMapper
from f1_analytics_platform.models import Race


class RaceClient:
    def __init__(self, http_client: BaseHttpClient):
        self._http_client = http_client
        self._mapper = RaceMapper()

    def get_races(self, season: int) -> list[Race]:
        response_json = self._http_client.get(f"/{season}/races.json")
        return self._mapper.map(response_json)
