"""
MLflow Experiment Tracking for External POE
Tracks Addition, Subtraction, Multiplication, and Division operations with MLflow.
"""
import os
import sys
import time
import mlflow

from main import add, subtract, multiply, divide


def setup_mlflow():
    """Configure MLflow tracking URI and experiment."""
    if os.path.exists("mlflow.db"):
        mlflow.set_tracking_uri("sqlite:///mlflow.db")
    
    experiment_name = "External-POE-MLDevOps"
    mlflow.set_experiment(experiment_name)
    print(f"[INFO] MLflow Tracking URI: {mlflow.get_tracking_uri()}")
    print(f"[INFO] Active Experiment:   {experiment_name}")
    return experiment_name


def track_arithmetic_runs():
    """Track sample operations: Addition, Subtraction, Multiplication, Division."""
    operations = [
        {"name": "operation_addition", "op": "addition", "num1": 20.0, "num2": 5.0, "func": add},
        {"name": "operation_subtraction", "op": "subtraction", "num1": 20.0, "num2": 5.0, "func": subtract},
        {"name": "operation_multiplication", "op": "multiplication", "num1": 20.0, "num2": 5.0, "func": multiply},
        {"name": "operation_division", "op": "division", "num1": 20.0, "num2": 5.0, "func": divide},
    ]

    for op in operations:
        with mlflow.start_run(run_name=op["name"]):
            start_t = time.perf_counter()
            result = op["func"](op["num1"], op["num2"])
            exec_time_ms = (time.perf_counter() - start_t) * 1000

            # Log parameters
            mlflow.log_param("operation", op["op"])
            mlflow.log_param("num1", op["num1"])
            mlflow.log_param("num2", op["num2"])

            # Log metrics
            mlflow.log_metric("result", result)
            mlflow.log_metric("execution_time_ms", round(exec_time_ms, 4))
            mlflow.log_metric("accuracy", 1.0)

            # Set tags
            mlflow.set_tag("project", "External-POE-MLDevOps")
            mlflow.set_tag("task", f"Arithmetic-{op['op'].capitalize()}")
            print(f"[SUCCESS] Logged {op['op'].capitalize()}: {op['num1']} and {op['num2']} -> {result}")


def main():
    print("==================================================")
    print("  MLflow Tracking: Add, Subtract, Multiply, Divide")
    print("==================================================")
    setup_mlflow()
    track_arithmetic_runs()
    print("==================================================")
    print("All 4 arithmetic operations logged to MLflow!")
    print("Refresh your browser at: http://127.0.0.1:5000")
    print("==================================================")


if __name__ == "__main__":
    main()
