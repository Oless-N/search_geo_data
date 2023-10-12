from sqlalchemy import func

from gisdatabase import database
from models.geodata import GeoData


async def search_by_region(region: str):
    query = f"""select * from geotable where region='{region}'"""

    results = await database.fetch_all(query)

    return {'result': results}


async def search_location_by_coordinates(
        lon: float,
        lat: float,
        distance: int = 1000):

    query = f"""
            SELECT *
            FROM geotable
            WHERE ST_DWithin(
                geometry,
                ST_SetSRID(ST_MakePoint({lon}, {lat}), 4326)::geography,
                {distance}
            );"""
    results = await database.fetch_all(query)
    return results


async def search_quadrangle(
    lon1,
    lat1,
    lon2,
    lat2,
    lon3,
    lat3,
    lon4,
    lat4,
):

    query = f"""SELECT *
        FROM geotable
        WHERE ST_Contains(
            ST_MakePolygon(
                ST_MakeLine(
                    ARRAY[
                        ST_SetSRID(ST_MakePoint('{lon1}', '{lat1}'), 4326),
                        ST_SetSRID(ST_MakePoint('{lon2}', '{lat2}'), 4326),
                        ST_SetSRID(ST_MakePoint('{lon3}', '{lat3}'), 4326),
                        ST_SetSRID(ST_MakePoint('{lon4}', '{lat4}'), 4326),
                        ST_SetSRID(ST_MakePoint('{lon1}', '{lat1}'), 4326)
                    ]
                )
            ),
            geometry
        );"""
    results = await database.fetch_all(query)
    return results