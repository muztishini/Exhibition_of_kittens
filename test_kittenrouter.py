from fastapi.testclient import TestClient
from main import app
from models import SessionLocal, Kitten
from typing import List, Dict

client = TestClient(app)


def last_kitten_id():
    db = SessionLocal()
    kitten = db.query(Kitten).order_by(Kitten.id.desc()).first()
    kitten_id = kitten.id if kitten else None
    return kitten_id


def test_read_kittens():
    response = client.get("/api/kittens")
    assert response.status_code == 200
    assert isinstance(response.json(), List)


def test_read_kitten():
    response = client.get("/api/kittens/1")
    assert response.status_code == 200
    assert isinstance(response.json(), Dict)


def test_create_kitten():
    response = client.post(
        "/api/kittens",
        json={
            "name": "string",
            "age": 1,
            "color": "string",
            "description": "string",
            "breed_id": 1})
    assert response.status_code == 200
    assert isinstance(response.json(), Dict)


def test_update_kitten():
    response = client.put(
        f"/api/kittens/{last_kitten_id()}/",
        json={
            "name": "string",
            "age": 1,
            "color": "string",
            "description": "string",
            "breed_id": 1},
    )
    assert response.status_code == 200
    assert isinstance(response.json(), Dict)


def test_delete_kitten():
    response = client.delete(f"/api/kittens/{last_kitten_id()}")
    assert response.status_code == 200
