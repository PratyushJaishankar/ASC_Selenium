import pytest

from Class_10_Oct_2025.src.Calculator import Calculator


@pytest.mark.parametrize("a,b,expected", [

    (1, 2, 3),

    (0, 0, 0),

    (-1, 1, 0),

    (10, -5, 5),

    (2.5, 3.5, 6.0)

])
def test_addition_parameterized(a, b, expected):
    calc = Calculator()

    result = calc.add(a, b)

    assert result == expected


@pytest.mark.parametrize("input,expected", [

    (0, True),

    (1, False),

    (2, True),

    (3, False),

    (4, True),

    (-2, True)  # Negative even numbers

])
def test_is_even_parameterized(input, expected):
    calc = Calculator()

    result = calc.is_even(input)

    assert result == expected