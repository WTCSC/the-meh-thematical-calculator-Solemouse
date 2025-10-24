import pytest
from MehCalculator import add, subtract, multiply, divide, exponent

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
def test_subtract_lead_to_negative():
    assert subtract(175, 225) == -50


def test_multiply_two_pos():
    assert multiply(8, 3) == 24
def test_multiply_two_two_digit_pos():
    assert multiply(87, 35) == 3045
def test_multiply_two_decimal():
    assert multiply(6.75, 3.93) == 26.5275
def test_multiply_by_zero():
    assert multiply(15, 0) == 0

def test_divide_by_two_pos():
    assert divide(8, 5) == 1.6
def test_divide_by_two_two_digit_pos():
    assert divide(75, 30) == 2.5
def test_divide_by_two_pos():
    assert divide(8, 5) == 1.6
def test_divide_by_one():
    assert divide(8, 1) == 8
def test_divide_by_zero():
    assert divide(8, 0) == False

def test_power_one():
    assert exponent(5, 1) == 5
def test_power_two():
    assert exponent(5, 5) == 3125
def test_power_zero():
    assert exponent(5, 0) == 1
