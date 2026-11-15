"""
Addition Program with FastAPI Integration.
Accepts two numbers and displays/returns their Addition.
"""
import sys
from fastapi import FastAPI, Query

app = FastAPI(title="Addition Service")


def add(num1: float, num2: float) -> float:
    """Returns the addition of two numbers."""
    return num1 + num2


@app.get("/")
def home():
    return {"message": "Addition Service API", "docs": "/docs"}


@app.get("/add")
def add_endpoint(num1: float = Query(..., description="First number"), num2: float = Query(..., description="Second number")):
    """FastAPI endpoint to add two numbers."""
    return {"num1": num1, "num2": num2, "sum": add(num1, num2)}


if __name__ == "__main__":
    if len(sys.argv) == 3:
        n1, n2 = float(sys.argv[1]), float(sys.argv[2])
    else:
        try:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
        except (ValueError, EOFError):
            n1, n2 = 10.0, 20.0
    print(f"Addition of {n1} and {n2} is: {add(n1, n2)}")
