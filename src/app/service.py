from serpapi import GoogleSearch
from starlette import status


def search_query_google(query: str, api_key) -> dict:

    try:
        params = {
            "engine": "google",
            "q": query,
            "api_key": api_key,
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        link = results['organic_results'][0]['link']
        title = results['organic_results'][0]['title']
        snippet = results['organic_results'][0]['snippet']

        dict_response = {
            'link': link,
            'title': title,
            'snippet': snippet,
        }
    except Exception:
        return status.HTTP_204_NO_CONTENT

    return dict_response


