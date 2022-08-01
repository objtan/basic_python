import pytest
import math

def test_sqrt_fails():
    num = 25
    assert math.sqrt(num) == 6

def test_square_fails():
    num = 7
    assert 7*7 == 40

def test_equals_fails():
    assert 10 == 11