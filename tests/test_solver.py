import pytest

from linearsolver import solve, SolveResult
from linearsolver.exceptions import (
    InconsistentSystemError,
    InfiniteSolutionsError,
)


def test_solve_gaussian():
    A = [[2, 1], [1, -1]]
    b = [5, 1]

    result = solve(A, b)

    assert isinstance(result, SolveResult)
    assert result.solution == pytest.approx((2, 1))
    assert result.method == "gaussian"


def test_unknown_method():
    with pytest.raises(ValueError):
        solve([[1]], [2], method="unknown")


def test_result_immutable():
    result = solve([[2]], [4])

    with pytest.raises(AttributeError):
        result.solution = (5,)


def test_fixed_unique():
    result = solve(
        [[1, 1, 1], [2, 2, 2]],
        [6, 12],
        fixed={1: 2, 2: 1},
    )

    assert result.solution == pytest.approx((3, 2, 1))


def test_fixed_insufficient():
    with pytest.raises(InfiniteSolutionsError):
        solve(
            [[1, 1, 1]],
            [6],
            fixed={2: 1},
        )


def test_fixed_inconsistent():
    with pytest.raises(InconsistentSystemError):
        solve(
            [[1, 1]],
            [3],
            fixed={0: 2, 1: 2},
        )


def test_general_unique():
    result = solve(
        [[1, 0], [0, 1], [1, 1]],
        [2, 3, 5],
        method="general",
    )

    assert result.solution == pytest.approx((2, 3))
