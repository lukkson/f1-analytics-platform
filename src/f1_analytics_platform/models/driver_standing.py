from pydantic import Field

from f1_analytics_platform.models import Driver
from f1_analytics_platform.models.base import F1BaseModel


class Constructor(F1BaseModel):
    constructor_id: str = Field(alias="constructorId")


class DriverStandings(F1BaseModel):
    wins: int
    position: int
    points: float
    driver: Driver = Field(alias="Driver")
    constructor: list[Constructor] = Field(alias="Constructors")


class DriverStanding(F1BaseModel):
    season: int
    round: int
    driver_standings: list[DriverStandings] = Field(alias="DriverStandings")
