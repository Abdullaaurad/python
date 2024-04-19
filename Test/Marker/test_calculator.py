# test_calculator.py
import pytest
from calculator import add, subtract

@pytest.mark.symbol1
def test_addition1():
    result = add(3, 5)
    assert result == 8

@pytest.mark.symbol1
def test_subtraction1():
    result = subtract(10, 5)
    assert result == 5

@pytest.mark.symbol2
def test_addition2():
    result = add(3, 5)
    assert result == 8

@pytest.mark.symbol2
def test_subtraction2():
    result = subtract(10, 2)
    assert result == 5

def test_multiplication():
    result = 2 * 3
    assert result == 6


# to run specific section we need we can give them names and by grouping by name we can run the function 
# pytest -v -m symbol1
# pytest -m symbol test_calculator.py
