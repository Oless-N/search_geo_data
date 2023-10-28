from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.dialects.postgresql import JSONB
from geoalchemy2 import Geometry
from .base import Base


class GeoData(Base):
    __tablename__ = 'geotable'
    id = Column(
        Integer,
        primary_key=True,
    )
    geometry = Column(Geometry(srid=4326))
    area_ha = Column(Float)
    crop = Column(String)
    history = Column(JSONB)
    productivity = Column(Float)
    region = Column(String)
    score = Column(String)
    type = Column(String)
