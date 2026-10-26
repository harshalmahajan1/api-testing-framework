
import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture
def api_client():
    """Provide a reusable HTTP session for API tests."""
    with requests.Session() as session:
        yield session


def test_get_post_returns_success(api_client):
    response = api_client.get(f"{BASE_URL}/posts/1", timeout=10)

    assert response.status_code == 200


def test_get_post_returns_valid_json(api_client):
    response = api_client.get(f"{BASE_URL}/posts/1", timeout=10)
    data = response.json()

    assert isinstance(data, dict)
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data


def test_get_missing_post_returns_empty_object(api_client):
    response = api_client.get(
        f"{BASE_URL}/posts/999999", timeout=10
    )

    assert response.status_code == 404
    assert response.json() == {}


def test_create_post_returns_created_resource(api_client):
    payload = {
        "title": "API testing practice",
        "body": "Learning automated API testing with pytest",
        "userId": 1,
    }

    response = api_client.post(
        f"{BASE_URL}/posts",
        json=payload,
        timeout=10,
    )

    assert response.status_code == 201

    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data


def test_get_post_rejects_invalid_id(api_client):
    response = api_client.get(
        f"{BASE_URL}/posts/invalid", timeout=10
    )

    assert response.status_code == 404
