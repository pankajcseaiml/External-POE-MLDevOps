"""
Pytest Unit and API tests for Addition Program.
"""
from fastapi.testclient import TestClient
from main import app, add

client = TestClient(app)


def test_addition():
    assert add(5, 3) == 8.0
    assert add(-4, 9) == 5.0
    assert add(-2, -7) == -9.0
    assert add(2.5, 4.5) == 7.0


def test_api_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Addition Service API"


def test_api_add():
    response = client.get("/add?num1=15&num2=25")
    assert response.status_code == 200
    data = response.json()
    assert data["num1"] == 15.0
    assert data["num2"] == 25.0
    assert data["sum"] == 40.0
