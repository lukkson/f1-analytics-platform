from f1_analytics_platform.extraction.http_client import HttpClient, BaseHttpClient
from f1_analytics_platform.extraction.mappers.standing_mapper import StandingMapper
from f1_analytics_platform.models import DriverStanding


class StandingsClient:
    def __init__(self, http_client: BaseHttpClient):
        self._http_client = http_client
        self._mapper = StandingMapper()

    def get_standings(self, season: int, round: int) -> list[DriverStanding]:
        response = self._http_client.get(f"/{season}/{round}/driverStandings.json")
        return self._mapper.map(response)
