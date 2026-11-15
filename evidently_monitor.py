# evidently_monitor.py
"""
Evidently AI Monitoring Tool Configuration
Monitors the Multiplication Service inputs (num1, num2) and output (multiplication_result).
Detects data drift and tracks data quality between baseline operations and production requests.
"""
import os
import sys
import numpy as np
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset, DataSummaryPreset
from main import multiply


def generate_multiplication_datasets(n_samples: int = 200):
    """
    Generate baseline (reference) and live production (current) datasets for multiplication requests.
    - Reference Dataset: Standard operational multiplication requests (numbers between 1 and 50).
    - Current Dataset: Production traffic simulating data drift (scale shift towards larger numbers).
    """
    np.random.seed(42)

    # Reference Dataset (Normal baseline usage)
    ref_num1 = np.random.uniform(low=1.0, high=50.0, size=n_samples)
    ref_num2 = np.random.uniform(low=1.0, high=50.0, size=n_samples)
    ref_results = [multiply(a, b) for a, b in zip(ref_num1, ref_num2)]

    reference_df = pd.DataFrame({
        "num1": np.round(ref_num1, 2),
        "num2": np.round(ref_num2, 2),
        "multiplication_result": np.round(ref_results, 2),
    })

    # Current Dataset (Production requests with simulated data drift: higher scale numbers)
    curr_num1 = np.random.uniform(low=100.0, high=500.0, size=n_samples)  # Drifted inputs
    curr_num2 = np.random.uniform(low=10.0, high=80.0, size=n_samples)
    curr_results = [multiply(a, b) for a, b in zip(curr_num1, curr_num2)]

    current_df = pd.DataFrame({
        "num1": np.round(curr_num1, 2),
        "num2": np.round(curr_num2, 2),
        "multiplication_result": np.round(curr_results, 2),
    })

    return reference_df, current_df


def run_evidently_monitoring(output_html: str = "evidently_report.html"):
    """
    Execute Evidently AI data drift and summary analysis on multiplication inputs/outputs
    and save an interactive HTML dashboard.
    """
    print("==================================================")
    print("  Evidently AI Tool - Multiplication Monitoring   ")
    print("==================================================")

    ref_data, curr_data = generate_multiplication_datasets()
    print(f"[INFO] Reference operations: {ref_data.shape[0]} requests (Columns: {list(ref_data.columns)})")
    print(f"[INFO] Current production operations: {curr_data.shape[0]} requests")
    print(f"[INFO] Baseline average product:   {ref_data['multiplication_result'].mean():.2f}")
    print(f"[INFO] Production average product: {curr_data['multiplication_result'].mean():.2f}")

    print("[INFO] Computing Data Drift and Data Summary metrics...")
    presets = [DataDriftPreset(), DataSummaryPreset()]
    report = Report(metrics=presets)
    report_result = report.run(reference_data=ref_data, current_data=curr_data)

    # Save to interactive HTML dashboard
    report_result.save_html(output_html)

    print(f"[SUCCESS] Evidently report generated successfully: {output_html}")
    full_path = os.path.abspath(output_html)
    print(f"[REPORT LOCATION] {full_path}")
    print("==================================================")
    return full_path


if __name__ == "__main__":
    report_file = "evidently_report.html"
    if len(sys.argv) > 1:
        report_file = sys.argv[1]
    run_evidently_monitoring(report_file)
