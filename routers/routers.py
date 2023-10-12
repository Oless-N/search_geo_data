from fastapi import APIRouter

from config import prefix
from controllers.geo_search import (
    search_by_region,
    search_location_by_coordinates, search_quadrangle,
)
from schemas.queries import SearchByRegion, NearbySearchQuery, ParallelogramQuery

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


@router.get("/search_quadrangle")
async def search_location(query: ParallelogramQuery):
    ret = await search_quadrangle(
        query.vertex1.lon,
        query.vertex1.lat,
        query.vertex2.lon,
        query.vertex2.lat,
        query.vertex3.lon,
        query.vertex3.lat,
        query.vertex4.lon,
        query.vertex4.lat,
    )
    return ret

