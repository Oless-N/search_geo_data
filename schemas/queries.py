from pydantic import BaseModel, validator, confloat, conint


class NearbySearchQuery(BaseModel):
    lon: confloat(ge=-180, le=180)
    lat: confloat(ge=-90, le=90)
    radius: conint(gt=0, le=22000)

    @validator("radius")
    def validate_radius(cls, value):
        if value > 10000:  # Як приклад, обмежимо радіус пошуку 10 км
            raise ValueError("Maximum allowed search radius is 10000 meters.")
        return value


class SearchByRegion(BaseModel):
    region: str

    @validator("region")
    def validate_region(cls, value):
        if value == "":
            raise ValueError("Region must be provided")
        return value


class Vertex(BaseModel):
    lon: confloat(ge=-180, le=180)
    lat: confloat(ge=-90, le=90)


class ParallelogramQuery(BaseModel):
    vertex1: Vertex
    vertex2: Vertex
    vertex3: Vertex
    vertex4: Vertex
