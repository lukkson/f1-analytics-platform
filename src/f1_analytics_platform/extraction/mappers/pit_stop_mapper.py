from f1_analytics_platform.models import PitStop


class PitStopMapper:
    def map(self, response: dict) -> list[PitStop]:
        pitstops = response["MRData"]["RaceTable"]["Races"]
        return [PitStop(**pitstop) for pitstop in pitstops]
