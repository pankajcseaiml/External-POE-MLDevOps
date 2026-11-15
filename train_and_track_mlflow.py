# train_and_track_mlflow.py
"""
MLflow Model Training and Experiment Tracking
Tracks model training, hyperparameters, evaluation metrics, and model artifacts
using the Diabetes Disease Progression dataset.
"""
import math
import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import mlflow
import mlflow.sklearn


def train_and_log_model(alpha: float = 0.5, test_size: float = 0.2, random_state: int = 42):
    """
    Train a Ridge regression model and log parameters, metrics, and the model artifact to MLflow.
    """
    print("==================================================")
    print("  MLflow Experiment Tracking - Model Training    ")
    print("  Dataset: Scikit-Learn Diabetes Progression      ")
    print("==================================================")

    # 1. Load data
    diabetes = load_diabetes(as_frame=True)
    X = diabetes.data
    y = diabetes.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    print(f"[INFO] Train samples: {X_train.shape[0]}, Test samples: {X_test.shape[0]}")

    # 2. Set experiment name
    experiment_name = "Internal-POE-MLDevOps"
    mlflow.set_experiment(experiment_name)

    # 3. Train & track run in MLflow
    with mlflow.start_run(run_name="ridge_regression_baseline") as run:
        run_id = run.info.run_id
        print(f"[INFO] Active MLflow Run ID: {run_id}")

        # Train model
        model = Ridge(alpha=alpha)
        model.fit(X_train, y_train)

        # Predictions & metrics
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        rmse = math.sqrt(mse)
        mae = mean_absolute_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        # Log parameters
        mlflow.log_param("model_type", "Ridge")
        mlflow.log_param("alpha", alpha)
        mlflow.log_param("test_size", test_size)
        mlflow.log_param("random_state", random_state)
        mlflow.log_param("n_features", X.shape[1])

        # Log metrics
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2_score", r2)

        # Log model artifact
        mlflow.sklearn.log_model(model, name="diabetes_model")

        # Set tags
        mlflow.set_tag("framework", "scikit-learn")
        mlflow.set_tag("project", "Internal-POE-MLDevOps")

        print("--------------------------------------------------")
        print(f"[METRIC] Mean Squared Error (MSE):     {mse:.4f}")
        print(f"[METRIC] Root Mean Squared Error (RMSE): {rmse:.4f}")
        print(f"[METRIC] Mean Absolute Error (MAE):     {mae:.4f}")
        print(f"[METRIC] R2 Determination Score:        {r2:.4f}")
        print("--------------------------------------------------")
        print(f"[SUCCESS] Run logged under experiment '{experiment_name}'")
        print("To view dashboard, run: mlflow ui")
        print("==================================================")

        return run_id, mse, r2


if __name__ == "__main__":
    train_and_log_model()
