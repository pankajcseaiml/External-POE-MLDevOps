import sys
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="Arithmetic Operations API (Add, Subtract, Multiply, Divide)",
    description="FastAPI service for all 4 operations: Addition, Subtraction, Multiplication, and Division.",
    version="1.0.0"
)

# Core Arithmetic Functions
def add(a: float, b: float) -> float: return a + b
def subtract(a: float, b: float) -> float: return a - b
def multiply(a: float, b: float) -> float: return a * b
def divide(a: float, b: float) -> float:
    if b == 0: raise ValueError("Division by zero is not allowed.")
    return a / b

# Schemas
class ArithmeticRequest(BaseModel):
    num1: float = Field(..., description="First number")
    num2: float = Field(..., description="Second number")

class OperationResponse(BaseModel):
    num1: float
    num2: float
    operation: str
    result: float

class AllOperationsResponse(BaseModel):
    num1: float
    num2: float
    addition: float
    subtraction: float
    multiplication: float
    division: float | None

# Endpoints
@app.get("/", tags=["All Operations"], response_model=AllOperationsResponse)
def calculate_all(num1: float = 0, num2: float = 0):
    div_res = divide(num1, num2) if num2 != 0 else None
    return AllOperationsResponse(
        num1=num1, num2=num2,
        addition=add(num1, num2),
        subtraction=subtract(num1, num2),
        multiplication=multiply(num1, num2),
        division=div_res
    )

@app.post("/calculate", tags=["All Operations"], response_model=AllOperationsResponse)
def calculate_all_post(req: ArithmeticRequest):
    div_res = divide(req.num1, req.num2) if req.num2 != 0 else None
    return AllOperationsResponse(
        num1=req.num1, num2=req.num2,
        addition=add(req.num1, req.num2),
        subtraction=subtract(req.num1, req.num2),
        multiplication=multiply(req.num1, req.num2),
        division=div_res
    )

@app.get("/add", tags=["Addition"], response_model=OperationResponse)
def api_add_get(num1: float = 0, num2: float = 0):
    return OperationResponse(num1=num1, num2=num2, operation="addition", result=add(num1, num2))

@app.post("/add", tags=["Addition"], response_model=OperationResponse)
def api_add_post(req: ArithmeticRequest):
    return OperationResponse(num1=req.num1, num2=req.num2, operation="addition", result=add(req.num1, req.num2))

@app.get("/subtract", tags=["Subtraction"], response_model=OperationResponse)
def api_sub_get(num1: float = 0, num2: float = 0):
    return OperationResponse(num1=num1, num2=num2, operation="subtraction", result=subtract(num1, num2))

@app.post("/subtract", tags=["Subtraction"], response_model=OperationResponse)
def api_sub_post(req: ArithmeticRequest):
    return OperationResponse(num1=req.num1, num2=req.num2, operation="subtraction", result=subtract(req.num1, req.num2))

@app.get("/multiply", tags=["Multiplication"], response_model=OperationResponse)
def api_mul_get(num1: float = 0, num2: float = 0):
    return OperationResponse(num1=num1, num2=num2, operation="multiplication", result=multiply(num1, num2))

@app.post("/multiply", tags=["Multiplication"], response_model=OperationResponse)
def api_mul_post(req: ArithmeticRequest):
    return OperationResponse(num1=req.num1, num2=req.num2, operation="multiplication", result=multiply(req.num1, req.num2))

@app.get("/divide", tags=["Division"], response_model=OperationResponse)
def api_div_get(num1: float = 0, num2: float = 0):
    if num2 == 0: raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
    return OperationResponse(num1=num1, num2=num2, operation="division", result=divide(num1, num2))

@app.post("/divide", tags=["Division"], response_model=OperationResponse)
def api_div_post(req: ArithmeticRequest):
    if req.num2 == 0: raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
    return OperationResponse(num1=req.num1, num2=req.num2, operation="division", result=divide(req.num1, req.num2))

if __name__ == "__main__":
    n1 = float(sys.argv[1]) if len(sys.argv) > 1 else float(input("Enter first number: "))
    n2 = float(sys.argv[2]) if len(sys.argv) > 2 else float(input("Enter second number: "))
    print(f"Addition:       {n1} + {n2} = {add(n1, n2)}")
    print(f"Subtraction:    {n1} - {n2} = {subtract(n1, n2)}")
    print(f"Multiplication: {n1} * {n2} = {multiply(n1, n2)}")
    print(f"Division:       {n1} / {n2} = {divide(n1, n2) if n2 != 0 else 'Error: Division by zero'}")
