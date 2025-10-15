
import pytest

from Class_10_Oct_2025.src.Calculator import Calculator



@pytest.mark.parametrize("operation,a,b,expected", [

    ("add", 5, 3, 8),

    ("subtract", 10, 4, 6),

    ("multiply", 6, 7, 42),

    ("divide", 15, 3, 5.0)

])

def test_all_operations(operation, a, b, expected):

    calc = Calculator()



    if operation == "add":

        result = calc.add(a, b)

    elif operation == "subtract":

        result = calc.subtract(a, b)

    elif operation == "multiply":

        result = calc.multiply(a, b)

    elif operation == "divide":

        result = calc.divide(a, b)



    assert result == expected



# Parameterizing with different input types

@pytest.mark.parametrize("input_number,expected_factorial", [

    (0, 1),

    (1, 1),

    (2, 2),

    (3, 6),

    (4, 24),

    (5, 120)

])

def test_factorial_parameterized(input_number, expected_factorial):

    calc = Calculator()

    result = calc.factorial(input_number)

    assert result == expected_factorial