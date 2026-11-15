"""
MLflow Experiment Tracking & Model Training for External POE
Tracks multiplication runs and regression model experiments using MLflow.
"""
import os
import sys
import time
import math
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import mlflow
import mlflow.sklearn

from main import multiply


def setup_mlflow():
    """Configure MLflow tracking URI and experiment."""
    # Point to local SQLite database if present, otherwise default to local ./mlruns
    if os.path.exists("mlflow.db"):
        mlflow.set_tracking_uri("sqlite:///mlflow.db")
    
    experiment_name = "External-POE-MLDevOps"
    mlflow.set_experiment(experiment_name)
    print(f"[INFO] MLflow Tracking URI: {mlflow.get_tracking_uri()}")
    print(f"[INFO] Active Experiment:   {experiment_name}")
    return experiment_name


def track_multiplication_runs():
    """Track sample multiplication runs with parameters and metrics."""
    test_cases = [
        {"run_name": "multiplication_basic", "num1": 6.0, "num2": 7.0, "scale": "small"},
        {"run_name": "multiplication_medium", "num1": 45.0, "num2": 80.0, "scale": "medium"},
        {"run_name": "multiplication_large", "num1": 250.0, "num2": 400.0, "scale": "large"},
    ]

    for tc in test_cases:
        with mlflow.start_run(run_name=tc["run_name"]):
            start_t = time.perf_counter()
            product = multiply(tc["num1"], tc["num2"])
            exec_time_ms = (time.perf_counter() - start_t) * 1000

            # Log parameters
            mlflow.log_param("operation", "multiplication")
            mlflow.log_param("num1", tc["num1"])
            mlflow.log_param("num2", tc["num2"])
            mlflow.log_param("scale", tc["scale"])

            # Log metrics
            mlflow.log_metric("product", product)
            mlflow.log_metric("execution_time_ms", round(exec_time_ms, 4))
            mlflow.log_metric("accuracy", 1.0)

            # Set tags
            mlflow.set_tag("project", "External-POE-MLDevOps")
            mlflow.set_tag("task", "Multiplication-Tracking")
            print(f"[SUCCESS] Logged run '{tc['run_name']}': {tc['num1']} x {tc['num2']} = {product}")


def train_and_track_ml_model(alpha: float = 0.5):
    """Train a Ridge Regression model on multiplication data and track with MLflow."""
    with mlflow.start_run(run_name=f"multiplication_regression_alpha_{alpha}"):
        np.random.seed(42)
        X = np.random.uniform(1.0, 50.0, (200, 2))
        y = np.array([multiply(a, b) for a, b in X])

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = Ridge(alpha=alpha)
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        rmse = math.sqrt(mse)
        mae = mean_absolute_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        # Log parameters
        mlflow.log_param("model_type", "Ridge")
        mlflow.log_param("alpha", alpha)
        mlflow.log_param("n_samples", 200)

        # Log metrics
        mlflow.log_metric("mse", round(mse, 4))
        mlflow.log_metric("rmse", round(rmse, 4))
        mlflow.log_metric("mae", round(mae, 4))
        mlflow.log_metric("r2_score", round(r2, 4))

        # Log model artifact
        mlflow.sklearn.log_model(model, name="multiplication_model")

        mlflow.set_tag("project", "External-POE-MLDevOps")
        mlflow.set_tag("framework", "scikit-learn")

        print(f"[SUCCESS] Logged ML Model: MSE={mse:.4f}, R2={r2:.4f}")


def main():
    print("==================================================")
    print("    MLflow Experiment Tracking - External POE     ")
    print("==================================================")
    setup_mlflow()
    track_multiplication_runs()
    train_and_track_ml_model(alpha=0.5)
    train_and_track_ml_model(alpha=1.0)
    print("==================================================")
    print("All runs successfully logged to MLflow!")
    print("Refresh your browser at: http://127.0.0.1:5000")
    print("==================================================")


if __name__ == "__main__":
    main()
