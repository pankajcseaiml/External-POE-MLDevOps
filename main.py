import sys
from fastapi import FastAPI
app = FastAPI()
def add(a: float, b: float) -> float: return a + b
@app.get("/")
@app.get("/add")
def add_api(num1: float = 0, num2: float = 0):
    return {"num1": num1, "num2": num2, "sum": add(num1, num2)}
if __name__ == "__main__":
    n1 = float(sys.argv[1]) if len(sys.argv) > 1 else float(input("Enter first number: "))
    n2 = float(sys.argv[2]) if len(sys.argv) > 2 else float(input("Enter second number: "))
    print(f"Addition of {n1} and {n2} is: {add(n1, n2)}")