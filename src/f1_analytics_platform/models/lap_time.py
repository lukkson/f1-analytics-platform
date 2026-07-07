from pydantic import Field

from f1_analytics_platform.models.base import F1BaseModel


class Timings(F1BaseModel):
    driver_id: str = Field(alias="driverId")
    position: int
    time: str


class Laps(F1BaseModel):
    number: str
    timings: list[Timings] = Field(alias="Timings")


class LapTime(F1BaseModel):
    season: str
    round: str
    laps: list[Laps] = Field(alias="Laps")
