from pydantic import Field

from f1_analytics_platform.models.base import F1BaseModel


class PitStops(F1BaseModel):
    driver_id: str = Field(alias="driverId")
    lap: int
    stop: int
    duration: str


class PitStop(F1BaseModel):
    season: int
    round: int
    race_name: str = Field(alias="raceName")
    pit_stops: list[PitStops] = Field(alias="PitStops")
