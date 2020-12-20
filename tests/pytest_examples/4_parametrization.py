from contextlib import nullcontext as does_not_raise

import pytest


def digits_sum(num):
    result = 0

    while num > 0:
        digit = num % 10
        result += digit
        num //= 10

    return result


@pytest.mark.parametrize(
    'num,expected_digits_sum',
    [
        (13, 4),
        (10, 1),
        (201, 3)
    ]
)
def test_digits_sum(num, expected_digits_sum):
    """Табличные тесты"""
    assert digits_sum(num) == expected_digits_sum



@pytest.mark.parametrize(
    'example_input,expected_exception',
    [
        (3, does_not_raise()),
        (2, does_not_raise()),
        (1, does_not_raise()),
        (0, pytest.raises(ZeroDivisionError)),
    ],
)
def test_division(example_input, expected_exception):
    """Табличные тесты ловить иссключения"""
    with expected_exception:
        assert (6 / example_input) is not None
