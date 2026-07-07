from f1_analytics_platform.models import Driver


class DriverMapper:
    def map(self, response: dict) -> list[Driver]:
        drivers = response["MRData"]["DriverTable"]["Drivers"]
        return [Driver(**driver) for driver in drivers]
