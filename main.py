import sys
from fastapi import FastAPI
app = FastAPI(title="Multiplication Service API")
def multiply(a: float, b: float) -> float: return a * b
@app.get("/")
@app.get("/multiply")
def multiply_api(num1: float = 0, num2: float = 0):
    return {"num1": num1, "num2": num2, "product": multiply(num1, num2), "result": multiply(num1, num2)}
if __name__ == "__main__":
    n1 = float(sys.argv[1]) if len(sys.argv) > 1 else float(input("Enter first number: "))
    n2 = float(sys.argv[2]) if len(sys.argv) > 2 else float(input("Enter second number: "))
    print(f"Multiplication of {n1} and {n2} is: {multiply(n1, n2)}")
