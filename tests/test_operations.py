import pytest
from app.operations.operations import addition, subtraction, multiplication, division

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0

def test_subtraction():
    assert subtraction(5, 3) == 2
    assert subtraction(0, 5) == -5
    assert subtraction(-2, -2) == 0

def test_multiplication():
    assert multiplication(2, 3) == 6
    assert multiplication(-1, 5) == -5
    assert multiplication(0, 100) == 0

def test_division():
    assert division(6, 3) == 2
    assert division(-10, 2) == -5
    assert division(5, 2) == 2.5

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(5, 0)
