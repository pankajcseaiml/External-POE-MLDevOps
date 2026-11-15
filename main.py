# main.py
"""
Multiplication Program with FastAPI Integration
Accepts two numbers and displays/returns their multiplication.
Can be executed as an interactive CLI script or launched as a FastAPI web service.
"""
import sys
from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, Field

# Initialize FastAPI application
app = FastAPI(
    title="Multiplication Service API",
    description="A FastAPI application that accepts two numbers and calculates their multiplication.",
    version="1.0.0",
)


def multiply(num1: float, num2: float) -> float:
    """Core multiplication function for two numbers."""
    return num1 * num2


class MultiplicationRequest(BaseModel):
    num1: float = Field(..., description="First number to multiply")
    num2: float = Field(..., description="Second number to multiply")


class MultiplicationResponse(BaseModel):
    num1: float
    num2: float
    operation: str = "multiplication"
    result: float


@app.get("/", tags=["Health"])
def root():
    """Root endpoint providing service information."""
    return {
        "service": "Multiplication Service API",
        "status": "online",
        "endpoints": {
            "GET_multiply": "/multiply?num1=10&num2=5",
            "POST_multiply": "/multiply",
            "docs": "/docs",
        },
    }


@app.get("/multiply", response_model=MultiplicationResponse, tags=["Math"])
def multiply_get(
    num1: float = Query(..., description="First number"),
    num2: float = Query(..., description="Second number"),
):
    """GET endpoint: accept two numbers via query parameters and return multiplication."""
    res = multiply(num1, num2)
    return MultiplicationResponse(num1=num1, num2=num2, result=res)


@app.post("/multiply", response_model=MultiplicationResponse, tags=["Math"])
def multiply_post(request: MultiplicationRequest):
    """POST endpoint: accept two numbers via JSON body and return multiplication."""
    res = multiply(request.num1, request.num2)
    return MultiplicationResponse(num1=request.num1, num2=request.num2, result=res)


def run_cli():
    """Interactive command-line execution: accepts two numbers and displays multiplication."""
    print("==================================================")
    print("       Python Multiplication Program (CLI)        ")
    print("==================================================")
    try:
        if len(sys.argv) >= 3:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
        else:
            num1 = float(input("Enter first number:  "))
            num2 = float(input("Enter second number: "))

        result = multiply(num1, num2)
        print("--------------------------------------------------")
        print(f"Calculation: {num1} x {num2} = {result}")
        print(f"Multiplication Result: {result}")
        print("==================================================")
        return result
    except ValueError:
        print("[ERROR] Please enter valid numeric values.")
        sys.exit(1)


if __name__ == "__main__":
    if "--server" in sys.argv:
        import uvicorn
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
    else:
        run_cli()
