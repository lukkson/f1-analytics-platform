from dependency_injector import containers

from f1_analytics_platform.config.http_config import HttpClientConfig
from f1_analytics_platform.extraction.client.driver_client import DriverClient
from f1_analytics_platform.extraction.client.lap_time_client import LapTimeClient
from f1_analytics_platform.extraction.client.pit_stop_client import PitStopClient
from f1_analytics_platform.extraction.client.race_client import RaceClient
from f1_analytics_platform.extraction.client.standing_client import StandingsClient
from f1_analytics_platform.extraction.http_client import HttpClient


class ExtractionContainer:
    def __init__(self):
        self._config = HttpClientConfig()
        self._http_client = HttpClient(self._config)

    @property
    def race_client(self) -> RaceClient:
        return RaceClient(self._http_client)

    @property
    def driver_client(self) -> DriverClient:
        return DriverClient(self._http_client)

    @property
    def lap_client(self) -> LapTimeClient:
        return LapTimeClient(self._http_client)

    @property
    def pit_stop_client(self) -> PitStopClient:
        return PitStopClient(self._http_client)

    @property
    def standings_client(self) -> StandingsClient:
        return StandingsClient(self._http_client)


class ExtractionContainer2(containers.DeclarativeContainer):
    pass
    # config = providers.Singleton(HttpClientConfig)
    # http_client = providers.Singleton(HttpClient, config)
    # race_client = providers.Factory[RaceClient]
    # driver_client = providers.Factory(DriverClient, http_client)
    # lap_client = providers.Factory(LapTimeClient, http_client)
    # pit_stop_client = providers.Factory(PitStopClient, http_client)
    # standings_client = providers.Factory(StandingsClient, http_client)
