import pytest

@pytest.fixture
def input_value():
    input = 34
    return input

def test_divisiable_by_2(input_value):
    assert input_value % 2 == 0