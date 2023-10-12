from fastapi import APIRouter

from config import prefix
from controllers.geo_search import (
    search_by_region,
    search_location_by_coordinates,
)
from schemas.queries import SearchByRegion, NearbySearchQuery

router = APIRouter(prefix=prefix)


@router.get("/search_region")
async def search_location(query: SearchByRegion):
    ret = await search_by_region(
        query.region
    )
    return ret


@router.get("/search_nearby")
async def search_location(query: NearbySearchQuery):
    ret = await search_location_by_coordinates(
        query.lon,
        query.lat,
        query.radius,
    )
    return ret
