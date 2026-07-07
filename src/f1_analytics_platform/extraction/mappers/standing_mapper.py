from f1_analytics_platform.models import DriverStanding


class StandingMapper:
    def map(self, response: dict) -> list[DriverStanding]:
        standings = response["MRData"]["StandingsTable"]["StandingsLists"]
        return [DriverStanding(**standing) for standing in standings]
