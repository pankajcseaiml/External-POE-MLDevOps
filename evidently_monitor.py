"""
Evidently AI Monitoring Tool for Addition Program.
Monitors input numbers (num1, num2) and their sum for data drift.
"""
import numpy as np
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset, DataSummaryPreset

from main import add


def generate_data(n_samples: int, low: float, high: float) -> pd.DataFrame:
    np.random.seed(42)
    num1 = np.random.uniform(low, high, n_samples)
    num2 = np.random.uniform(low, high, n_samples)
    sums = [add(n1, n2) for n1, n2 in zip(num1, num2)]
    return pd.DataFrame({"num1": num1, "num2": num2, "sum": sums})


def main():
    print("Generating Addition datasets for Evidently AI...")
    reference_data = generate_data(100, 1.0, 50.0)
    current_data = generate_data(100, 20.0, 100.0)

    report = Report(metrics=[DataDriftPreset(), DataSummaryPreset()])
    report_result = report.run(reference_data=reference_data, current_data=current_data)

    output_path = "evidently_report.html"
    report_result.save_html(output_path)
    print(f"Evidently report generated successfully: {output_path}")


if __name__ == "__main__":
    main()
