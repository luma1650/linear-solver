import pytest

from linearsolver import solve, SolveResult


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