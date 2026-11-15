# tests/test_hello.py
"""Test cases for hello.py application and MLflow pipeline."""
import sys
from pathlib import Path

# Add project root directory to sys.path so modules can be imported directly
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from hello import get_message, main
from train_and_track_mlflow import train_and_log_model


def test_hello_mlops_message(capsys):
    """Test 1: Verify get_message returns expected greeting and main prints it."""
    # Test function return value
    message = get_message()
    print(f"\n[PYTEST OUTPUT] get_message() returned: '{message}'")
    assert message == "Hello MLOps", f"Expected 'Hello MLOps', got '{message}'"

    # Test main() execution and standard output
    main()
    captured = capsys.readouterr()
    print(f"[PYTEST OUTPUT] captured stdout from main(): '{captured.out.strip()}'")
    assert "Hello MLOps" in captured.out


def test_mlflow_training_and_tracking():
    """Test 2: Verify MLflow model training, metrics calculation, and artifact logging."""
    run_id, mse, r2 = train_and_log_model()
    print(f"\n[PYTEST OUTPUT] MLflow logged Run ID: '{run_id}' with R2 Score: {r2:.4f}")
    assert run_id is not None and len(run_id) > 0
    assert mse > 0
    assert r2 > 0.3
