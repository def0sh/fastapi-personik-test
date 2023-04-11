import os
from dotenv import load_dotenv, find_dotenv
from fastapi.testclient import TestClient
import pytest
from src.app.service import search_query_google
from src.main import app


client = TestClient(app)


load_dotenv(find_dotenv())


@pytest.fixture
def api_key():
    return os.environ.get("SERP_API_KEY")


def test_search_query_google(api_key):
    query = "python"
    expected_response = {
        "link": "https://www.python.org/",
        "title": "Welcome to Python.org",
        "snippet": "The official home of the Python Programming Language."
    }
    assert search_query_google(query, api_key) == expected_response


def test_empty_search_query_google(api_key):
    query = ""
    expected_response = 204
    assert search_query_google(query, api_key) == expected_response


def test_get_search_result():
    response = client.get("/search/cat")
    assert response.status_code == 200
    assert "results" in response.json()



