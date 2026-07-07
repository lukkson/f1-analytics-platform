from pydantic import Field

from f1_analytics_platform.models.base import F1BaseModel


class Location(F1BaseModel):
    country: str


class Circuit(F1BaseModel):
    circuit_id: str = Field(alias="circuitId")
    circuit_name: str = Field(alias="circuitName")
    location: Location = Field(alias="Location")


class Race(F1BaseModel):
    season: int
    round: int
    circuit: Circuit = Field(alias="Circuit")
    race_name: str = Field(alias="raceName")
    date: str
