from code_example import Calc, Util
from re import U

def test_calc():
    cals = Calc()
    input = [1, 3, 4, 5]
    assert cals, sum(input) == 13

def test_util():
    util = Util()
    input = 'hello world'
    assert util.upper_case(input) == 'HELLO WORLD'