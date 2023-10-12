from fastapi import APIRouter

from config import prefix
from controllers.geo_search import search_by_region
from schemas.queries import SearchByRegion

router = APIRouter(prefix=prefix)


@router.get("/search_region")
async def search_location(query: SearchByRegion):
    ret = await search_by_region(
        query.region
    )
    return ret
