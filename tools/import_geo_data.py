import geojson
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
)
from geoalchemy2 import Geometry
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import sessionmaker, declarative_base

connection_url = 'postgresql://postgres_user:geodata1234@127.0.0.1:5444/postgres' # noqa
engine = create_engine(
    connection_url,
    pool_size=10,
    max_overflow=2,
    pool_recycle=300,
    pool_pre_ping=True,
    pool_use_lifo=True
    # echo=True,
)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class GeoData(Base):
    __tablename__ = 'geotable'

    id = Column(Integer, primary_key=True)
    geometry = Column(Geometry(srid=4326))
    area_ha = Column(Float)
    crop = Column(String)
    history = Column(JSONB)
    productivity = Column(String)
    region = Column(String)
    score = Column(String)
    type = Column(String)


GeoData.__table__.drop(bind=engine)
GeoData.__table__.create(bind=engine)


def geometry_to_ewkt(geom_dict):
    geom_type = geom_dict['type'].upper()
    if geom_type == 'POINT':
        coords = geom_dict['coordinates']
        return f'SRID=4326;POINT({coords[0]} {coords[1]})'
    elif geom_type == 'MULTIPOLYGON':
        polys = ','.join([','.join(
            [f"(({','.join([' '.join(map(str, point)) for point in points])}))"
             for points in poly]) for poly in geom_dict['coordinates']])
        return f'SRID=4326;MULTIPOLYGON({polys})'

count = 0
with engine.connect() as connection:
    with open('tools/fr-subset.geojsons') as f:
        for line in f:
            data = geojson.loads(line)

            geometry = None
            if data.get('geometry') is not None:
                geometry = geometry_to_ewkt(data['geometry'])

            geo_data = GeoData(
                geometry=geometry,
                id=data['properties']['id'],
                crop=data['properties']['crop'],
                productivity=data['properties']['productivity'],
                area_ha=float(data['properties']['area_ha']) if data['properties']['area_ha'] else None,  # noqa
                history=data['properties']['history'],
                region=data['properties']['region'],
                score=data['properties']['score'],
                type=data['geometry']['type'].upper(),
            )
            session.add(geo_data)
            count += 1

    session.commit()

print(f'total docs: {count}', 'Data imported successfully!')
