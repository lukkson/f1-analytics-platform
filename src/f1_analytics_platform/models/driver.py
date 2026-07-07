from typing import Optional

from pydantic import Field

from f1_analytics_platform.models.base import F1BaseModel


class Driver(F1BaseModel):
    driver_id: str = Field(alias="driverId")
    permanent_number: str = Field(alias="permanentNumber")
    code: Optional[str]
    given_name: str = Field(alias="givenName")
    family_name: str = Field(alias="familyName")
    date_of_birth: str = Field(alias="dateOfBirth")
    nationality: str
