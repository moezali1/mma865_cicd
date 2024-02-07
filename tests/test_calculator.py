# test_calculator.py

from calculator import add, subtract, multiply, divide
import pytest


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(8, 2) == 4
    # pytest.raises is used to check for exceptions
    with pytest.raises(ValueError):
        divide(8, 0)
