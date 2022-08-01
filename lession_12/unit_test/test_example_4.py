import pytest

@pytest.mark.parametrize('input, output', [(1,3), (2,6), (4,12), (8,24), (9,25)])
def test_multiply(input, output):
    assert input * 3 == output