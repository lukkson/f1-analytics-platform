from pydantic import BaseModel


class F1BaseModel(BaseModel):
    model_config = {"populate_by_name": True}
