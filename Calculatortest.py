import pytest
from MehCalculator.py import add, subtract, multiply, divide, exponent

def test_add_two_pos():
    assert add(8, 3) == 11
def test_add_two_two_digit_pos():
    assert add(87, 35) == 122
def test_add_two_decimal():
    assert add(6.75, 3.93) == 10.68

def test_subtract_two_pos():
    assert subtract(8, 3) == 5
def test_subtract_two_two_digit_pos():
    assert subtract(87, 35) == 52
def test_subtract_two_decimal():
    assert subtract(6.75, 3.93) == 2.82