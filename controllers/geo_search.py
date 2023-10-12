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
