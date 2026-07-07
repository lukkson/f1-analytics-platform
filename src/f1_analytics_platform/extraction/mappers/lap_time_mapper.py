from f1_analytics_platform.models import LapTime


class LapTimeMapper:
    def map(self, response: dict) -> list[LapTime]:
        lap_times = response["MRData"]["RaceTable"]["Races"]
        return [LapTime(**race) for race in lap_times]
