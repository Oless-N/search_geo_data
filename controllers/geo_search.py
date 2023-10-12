from sqlalchemy import func

from gisdatabase import database
from models.geodata import GeoData


async def search_by_region(region: str):
    # query = (
    #     GeoData.__table__.select()
    #     .where(
    #         func.region(region)
    #     )
    # )
    query = f"""select * from geotable where region='{region}'"""

    results = await database.fetch_all(query)

    return {'result': results}


async def search_location_by_coordinates(
        lon: float,
        lat: float,
        distance: int = 1000):

    query = (
        GeoData.__table__.select()
        .where(
            func.ST_DWithin(
                GeoData.geometry,
                func.ST_MakePoint(lon, lat),
                distance
            )
        )
    )
    results = await database.fetch_all(query)
    return results
