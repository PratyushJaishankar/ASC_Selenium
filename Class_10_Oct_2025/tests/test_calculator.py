from Class_10_Oct_2025.src.Calculator import Calculator
import pytest

@pytest.fixture
def calc():
    print("Creating Calculator instance")
    return Calculator()

def test_add(calc):
    print("Running test_add")
    result1 = calc.add(2, 3)
    print(f"calc.add(2, 3) = {result1}")
    assert result1 == 5
    result2 = calc.add(-1, 1)
    print(f"calc.add(-1, 1) = {result2}")
    assert result2 == 0

def test_subtract(calc):
    print("Running test_subtract")
    result1 = calc.subtract(5, 3)
    print(f"calc.subtract(5, 3) = {result1}")
    assert result1 == 2
    result2 = calc.subtract(0, 5)
    print(f"calc.subtract(0, 5) = {result2}")
    assert result2 == -5

def test_multiply(calc):
    print("Running test_multiply")
    result1 = calc.multiply(4, 3)
    print(f"calc.multiply(4, 3) = {result1}")
    assert result1 == 12
    result2 = calc.multiply(-2, 3)
    print(f"calc.multiply(-2, 3) = {result2}")
    assert result2 == -6

def test_divide(calc):
    print("Running test_divide")
    result1 = calc.divide(10, 2)
    print(f"calc.divide(10, 2) = {result1}")
    assert result1 == 5
    print("Testing division by zero")
    with pytest.raises(ValueError):
        calc.divide(5, 0)

def test_is_even(calc):
    print("Running test_is_even")
    result1 = calc.is_even(4)
    print(f"calc.is_even(4) = {result1}")
    assert result1 is True
    result2 = calc.is_even(5)
    print(f"calc.is_even(5) = {result2}")
    assert result2 is False

def test_factorial(calc):
    print("Running test_factorial")
    result1 = calc.factorial(0)
    print(f"calc.factorial(0) = {result1}")
    assert result1 == 1
    result2 = calc.factorial(5)
    print(f"calc.factorial(5) = {result2}")
    assert result2 == 120
    print("Testing factorial of negative number")
    with pytest.raises(ValueError):
        calc.factorial(-1)
