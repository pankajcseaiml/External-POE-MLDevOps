# tests/test_hello.py
"""Test case for multiplication application."""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from hello import get_multiplication_message, main
from main import multiply


def test_hello_multiplication(capsys):
    """Test multiplication greeting message and output."""
    message = get_multiplication_message(6.0, 7.0)
    print(f"\n[PYTEST OUTPUT] get_multiplication_message() returned: '{message}'")
    assert "42.0" in message

    main()
    captured = capsys.readouterr()
    print(f"[PYTEST OUTPUT] captured stdout: '{captured.out.strip()}'")
    assert "42.0" in captured.out
