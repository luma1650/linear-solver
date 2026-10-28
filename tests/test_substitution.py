import pytest

from linearsolver.core.substitution import back_substitution
from linearsolver.exceptions import SingularMatrixError


def test_basic_system():
    U = [
        [2, 1, -1],
        [0, 3, 2],
        [0, 0, 4],
    ]
    b = [3, 5, 8]

    x = back_substitution(U, b)

    assert x == pytest.approx((7 / 3, 1 / 3, 2))


def test_single_variable():
    assert back_substitution([[4]], [12]) == (3.0,)


def test_zero_pivot():
    U = [
        [1, 2],
        [0, 0],
    ]

    with pytest.raises(SingularMatrixError):
        back_substitution(U, [3, 0])


def test_immutable_input():
    U = ((2, 1), (0, 3))
    b = (5, 6)

    assert back_substitution(U, b) == pytest.approx((1.5, 2.0))