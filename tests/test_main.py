"""
Pytest Unit and API tests for All 4 Operations:
Addition, Subtraction, Multiplication, and Division.
"""
import pytest
from fastapi.testclient import TestClient
from main import app, add, subtract, multiply, divide

client = TestClient(app, base_url="http://127.0.0.1")


def test_addition():
    assert add(10, 5) == 15.0
    assert add(-4, 9) == 5.0
    assert add(0, 0) == 0.0


def test_subtraction():
    assert subtract(10, 5) == 5.0
    assert subtract(5, 10) == -5.0
    assert subtract(-2, -5) == 3.0


def test_multiplication():
    assert multiply(10, 5) == 50.0
    assert multiply(-4, 9) == -36.0
    assert multiply(2.5, 4.0) == 10.0


def test_division():
    assert divide(10, 5) == 2.0
    assert divide(9, 2) == 4.5
    with pytest.raises(ValueError):
        divide(10, 0)


def test_api_calculate_all():
    response = client.get("/?num1=20&num2=4")
    assert response.status_code == 200
    data = response.json()
    assert data["addition"] == 24.0
    assert data["subtraction"] == 16.0
    assert data["multiplication"] == 80.0
    assert data["division"] == 5.0


def test_api_endpoints():
    assert client.get("/add?num1=20&num2=4").json()["result"] == 24.0
    assert client.get("/subtract?num1=20&num2=4").json()["result"] == 16.0
    assert client.get("/multiply?num1=20&num2=4").json()["result"] == 80.0
    assert client.get("/divide?num1=20&num2=4").json()["result"] == 5.0


def test_api_division_by_zero():
    response = client.get("/divide?num1=20&num2=0")
    assert response.status_code == 400
