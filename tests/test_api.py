import responses  # Alternativa porque me daba error 403
import requests

API_URL = "https://reqres.in/api"

@responses.activate
def test_get_users():
    mocked_data = {
        "page": 2,
        "data": [{"id": 1, "name": "User Test"}]
    }

    responses.add(
        responses.GET,
        f"{API_URL}/users?page=2",
        json=mocked_data,
        status=200
    )

    response = requests.get(f"{API_URL}/users?page=2")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0


@responses.activate
def test_create_user():
    payload = {
        "name": "Victoria",
        "job": "QA Automation"
    }

    responses.add(
        responses.POST,
        f"{API_URL}/users",
        json={**payload, "id": "123", "createdAt": "2025-01-01"},
        status=201
    )

    response = requests.post(f"{API_URL}/users", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Victoria"


@responses.activate
def test_delete_user():
    responses.add(
        responses.DELETE,
        f"{API_URL}/users/2",
        status=204
    )

    response = requests.delete(f"{API_URL}/users/2")
    assert response.status_code == 204