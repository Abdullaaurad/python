import pytest
from Math import add

@pytest.mark.parametrize("num1, num2, result", [(1, 2, 3), (3, 4, 7), ("A", "B", "AB")])

def test_addition(num1, num2, result):
    assert add(num1, num2) == result
