from fastapi import APIRouter, Depends
from starlette import status

from .service import search_query_google
from ..config import Settings, get_settings

search_router = APIRouter(prefix='', tags=['Google query'])


@search_router.get('/search/{query}', summary="make a search query", status_code=200)
async def get_search_result(query: str, settings: Settings = Depends(get_settings)):
    """
    Make a search query to Google.com:
    - **query**: required
    """

    # search query to google
    response = search_query_google(query, api_key=settings.SERP_API_KEY)

    if response == status.HTTP_204_NO_CONTENT:
        return {
            "results": response,
            'detail': 'no search results'
        }
    return {
        "results": response}

