"""
Pytest Unit and API tests for Multiplication Program.
"""
from fastapi.testclient import TestClient
from main import app, multiply

client = TestClient(app, base_url="http://127.0.0.1")


def test_multiplication():
    assert multiply(5, 3) == 15.0
    assert multiply(-4, 9) == -36.0
    assert multiply(-2, -7) == 14.0
    assert multiply(2.5, 4.0) == 10.0
    assert multiply(0, 100) == 0.0


def test_api_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "product" in data


def test_api_multiply():
    response = client.get("/multiply?num1=6&num2=7")
    assert response.status_code == 200
    data = response.json()
    assert data["num1"] == 6.0
    assert data["num2"] == 7.0
    assert data["product"] == 42.0
