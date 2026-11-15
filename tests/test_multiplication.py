# tests/test_multiplication.py
"""
Pytest Unit Tests for Multiplication Program and FastAPI Endpoints.
"""
import sys
from pathlib import Path
from fastapi.testclient import TestClient

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from main import app, multiply

client = TestClient(app)


def test_core_multiplication_positive():
    """Test 1: Core multiply function with positive numbers."""
    result = multiply(6, 7)
    print(f"\n[PYTEST OUTPUT] multiply(6, 7) = {result}")
    assert result == 42.0


def test_core_multiplication_negative_and_zero():
    """Test 2: Core multiply function with negative numbers and zero."""
    assert multiply(-5, 4) == -20.0
    assert multiply(-3, -8) == 24.0
    assert multiply(0, 100) == 0.0
    assert multiply(2.5, 4.0) == 10.0
    print("[PYTEST OUTPUT] Handled negative, zero, and float multiplications successfully.")


def test_fastapi_root_endpoint():
    """Test 3: FastAPI Root health/info endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "Multiplication Service API"
    assert data["status"] == "online"
    print(f"[PYTEST OUTPUT] GET / returned: {data['service']}")


def test_fastapi_get_multiply():
    """Test 4: FastAPI GET /multiply query parameters endpoint."""
    response = client.get("/multiply?num1=12.5&num2=4")
    assert response.status_code == 200
    data = response.json()
    assert data["num1"] == 12.5
    assert data["num2"] == 4.0
    assert data["result"] == 50.0
    print(f"[PYTEST OUTPUT] GET /multiply?num1=12.5&num2=4 returned: {data['result']}")


def test_fastapi_post_multiply():
    """Test 5: FastAPI POST /multiply JSON body endpoint."""
    payload = {"num1": 9.0, "num2": 8.0}
    response = client.post("/multiply", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 72.0
    print(f"[PYTEST OUTPUT] POST /multiply with {payload} returned: {data['result']}")


def test_fastapi_invalid_input():
    """Test 6: FastAPI input validation rejection on non-numeric types."""
    response = client.get("/multiply?num1=invalid&num2=5")
    assert response.status_code == 422  # Unprocessable Entity
    print("[PYTEST OUTPUT] FastAPI rejected non-numeric parameter with status 422 as expected.")
