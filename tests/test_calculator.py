import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from calculator import add, subtract, multiply, divide, power, square_root


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(5, 6) == 30


def test_divide():
    assert divide(20, 4) == 5

def test_power():
    assert power(2, 3) == 8

def test_square_root():
    assert square_root(16) == 4