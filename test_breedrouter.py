from fastapi.testclient import TestClient
from main import app
from typing import List

client = TestClient(app)


def test_read_breeds():
    response = client.get("/api/breeds")
    assert response.status_code == 200
    assert isinstance(response.json(), List)


def test_get_kittens_by_breed():
    response = client.get("/api/breeds/2")
    assert response.status_code == 200
    assert isinstance(response.json(), List)
    