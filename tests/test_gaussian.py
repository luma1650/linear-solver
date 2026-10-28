import pytest

from linearsolver.solvers.gaussian import solve_gaussian
from linearsolver.exceptions import SingularMatrixError


def test_3x3_system():
    A = [
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2],
    ]
    b = [8, -11, -3]

    assert solve_gaussian(A, b) == pytest.approx(
        (2, 3, -1)
    )


def test_2x2_system():
    A = [
        [2, 1],
        [1, -1],
    ]
    b = [5, 1]

    assert solve_gaussian(A, b) == pytest.approx(
        (2, 1)
    )


def test_1x1_system():
    assert solve_gaussian([[4]], [12]) == pytest.approx((3,))


def test_singular_system():
    A = [[1, 2], [2, 4]]
    b = [3, 6]

    with pytest.raises(SingularMatrixError):
        solve_gaussian(A, b)


def test_zero_initial_pivot():
    A = [
        [0, 2],
        [3, 4],
    ]
    b = [4, 11]

    assert solve_gaussian(A, b) == pytest.approx((1, 2))


def test_immutable_input():
    A = ((2, 1), (1, -1))
    b = (5, 1)

    assert solve_gaussian(A, b) == pytest.approx((2, 1))