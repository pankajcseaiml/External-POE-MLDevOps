import sys
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Arithmetic Operations API (Add, Subtract, Multiply, Divide)")

def add(a: float, b: float) -> float: return a + b
def subtract(a: float, b: float) -> float: return a - b
def multiply(a: float, b: float) -> float: return a * b
def divide(a: float, b: float) -> float:
    if b == 0: raise ValueError("Division by zero is not allowed.")
    return a / b

@app.get("/")
def calculate_all(num1: float = 0, num2: float = 0):
    div_res = divide(num1, num2) if num2 != 0 else None
    return {
        "num1": num1, "num2": num2,
        "addition": add(num1, num2),
        "subtraction": subtract(num1, num2),
        "multiplication": multiply(num1, num2),
        "division": div_res
    }

@app.get("/add")
def api_add(num1: float = 0, num2: float = 0):
    return {"num1": num1, "num2": num2, "operation": "addition", "result": add(num1, num2)}

@app.get("/subtract")
def api_sub(num1: float = 0, num2: float = 0):
    return {"num1": num1, "num2": num2, "operation": "subtraction", "result": subtract(num1, num2)}

@app.get("/multiply")
def api_mul(num1: float = 0, num2: float = 0):
    return {"num1": num1, "num2": num2, "operation": "multiplication", "result": multiply(num1, num2)}

@app.get("/divide")
def api_div(num1: float = 0, num2: float = 0):
    if num2 == 0: raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
    return {"num1": num1, "num2": num2, "operation": "division", "result": divide(num1, num2)}

if __name__ == "__main__":
    n1 = float(sys.argv[1]) if len(sys.argv) > 1 else float(input("Enter first number: "))
    n2 = float(sys.argv[2]) if len(sys.argv) > 2 else float(input("Enter second number: "))
    print(f"Addition:       {n1} + {n2} = {add(n1, n2)}")
    print(f"Subtraction:    {n1} - {n2} = {subtract(n1, n2)}")
    print(f"Multiplication: {n1} * {n2} = {multiply(n1, n2)}")
    print(f"Division:       {n1} / {n2} = {divide(n1, n2) if n2 != 0 else 'Error: Division by zero'}")
