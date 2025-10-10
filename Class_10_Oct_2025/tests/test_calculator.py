from Class_10_Oct_2025.src.Calculator import Calculator
import pytest

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 5) == -5

def test_multiply(calc):
    assert calc.multiply(4, 3) == 12
    assert calc.multiply(-2, 3) == -6

def test_divide(calc):
    assert calc.divide(10, 2) == 5
    with pytest.raises(ValueError):
        calc.divide(5, 0)

def test_is_even(calc):
    assert calc.is_even(4) is True
    assert calc.is_even(5) is False

def test_factorial(calc):
    assert calc.factorial(0) == 1
    assert calc.factorial(5) == 120
    with pytest.raises(ValueError):
        calc.factorial(-1)
