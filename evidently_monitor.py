# evidently_monitor.py
"""
Evidently AI Monitoring Tool Configuration
Step 12: Uses the real-world Diabetes Disease Progression dataset from scikit-learn,
evaluates data drift and data quality between baseline and production patient cohorts,
and generates an interactive HTML dashboard.
"""
import os
import sys
import pandas as pd
from sklearn.datasets import load_diabetes


def load_disease_dataset():
    """
    Load the standard medical Diabetes progression dataset from scikit-learn.
    Features include: age, sex, bmi, bp, and 6 blood serum measurements (s1-s6).
    Splits into reference (baseline cohort) and current (incoming production cohort).
    """
    diabetes = load_diabetes(as_frame=True)
    df = diabetes.frame

    # Split dataset into baseline reference cohort and current production cohort
    midpoint = len(df) // 2
    reference_df = df.iloc[:midpoint].copy().reset_index(drop=True)
    current_df = df.iloc[midpoint:].copy().reset_index(drop=True)

    return reference_df, current_df


def run_evidently_monitoring(output_html: str = "evidently_report.html"):
    """
    Run Evidently drift and summary metrics report and save interactive HTML dashboard.
    """
    print("==================================================")
    print("  Evidently AI Tool - Disease Data Monitoring     ")
    print("  Dataset: Scikit-Learn Diabetes Progression      ")
    print("==================================================")

    ref_data, curr_data = load_disease_dataset()
    print(f"[INFO] Features: {list(ref_data.columns)}")
    print(f"[INFO] Reference cohort (baseline): {ref_data.shape[0]} patient records")
    print(f"[INFO] Current cohort (production): {curr_data.shape[0]} patient records")

    # Import Report and Presets with compatibility fallback
    try:
        from evidently import Report
        from evidently.presets import DataDriftPreset, DataSummaryPreset
        presets = [DataDriftPreset(), DataSummaryPreset()]
    except (ImportError, AttributeError):
        try:
            from evidently.report import Report
            from evidently.metric_preset import DataDriftPreset, DataQualityPreset
            presets = [DataDriftPreset(), DataQualityPreset()]
        except ImportError:
            from evidently.legacy.report import Report
            from evidently.legacy.metric_preset import DataDriftPreset, DataQualityPreset
            presets = [DataDriftPreset(), DataQualityPreset()]

    print("[INFO] Computing Data Drift and Data Summary metrics...")
    report = Report(metrics=presets)
    report_result = report.run(reference_data=ref_data, current_data=curr_data)

    # Save to interactive HTML
    if hasattr(report_result, "save_html"):
        report_result.save_html(output_html)
    elif hasattr(report, "save_html"):
        report.save_html(output_html)

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
