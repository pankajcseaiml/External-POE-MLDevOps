# hello.py
"""
Multiplication Program - Core Module
Accepts two numbers and displays their multiplication.
"""
from main import multiply, run_cli


def get_multiplication_message(num1: float = 6.0, num2: float = 7.0) -> str:
    """Return formatted multiplication greeting."""
    result = multiply(num1, num2)
    return f"Multiplication of {num1} and {num2} is: {result}"


def main():
    """Execute multiplication program."""
    message = get_multiplication_message(6.0, 7.0)
    print(message)


if __name__ == "__main__":
    main()
