from fastapi.testclient import TestClient
from main import app
from typing import List

client = TestClient(app)


def test_read_breeds():
    response = client.get("/api/breeds")
    assert response.status_code == 200
    assert isinstance(response.json(), List)


def test_read_kittens():
    response = client.get("/api/kittens")
    assert response.status_code == 200
    assert isinstance(response.json(), List)
      