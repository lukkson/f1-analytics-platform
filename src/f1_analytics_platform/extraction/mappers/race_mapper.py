from f1_analytics_platform.models import Race


class RaceMapper:

    # def map(self, response: dict) -> list[Race]:
    #     races = response["MRData"]["RaceTable"]["Races"]
    #     return [
    #         Race(
    #             season=race["season"],
    #             round=race["round"],
    #             race_name=race["raceName"],
    #             circuit_id=race["Circuit"]["circuitId"],
    #             circuit_name=race["Circuit"]["circuitName"],
    #             country=race["Circuit"]["Location"]["country"],
    #             date=race["date"],
    #         )
    #         for race in races
    #     ]

    def map(self, response: dict) -> list[Race]:
        races = response["MRData"]["RaceTable"]["Races"]
        return [Race(**race) for race in races]
