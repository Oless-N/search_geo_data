from pydantic import BaseModel, validator


class SearchQuery(BaseModel):
    lon: float
    lat: float
    distance: int = 1000

    @validator("distance")
    def validate_distance(cls, value):
        if value <= 0:
            raise ValueError("Distance must be greater than 0")
        return value


class SearchByRegion(BaseModel):
    region: str

    @validator("region")
    def validate_region(cls, value):
        if value == "":
            raise ValueError("Region must be provided")
        return value
