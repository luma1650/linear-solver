import pytest

from linearsolver.solvers.general import solve_general
from linearsolver.results import SolutionStatus


def test_unique_solution():
    A = [[2, 1], [1, -1]]
    b = [5, 1]

    result = solve_general(A, b)

    assert result.status == SolutionStatus.UNIQUE
    assert result.particular == pytest.approx((2, 1))
    assert result.rank == 2
    assert result.nullspace_basis == ()


def test_infinite_solutions():
    A = [[1, 2, 3], [2, 4, 6]]
    b = [6, 12]

    result = solve_general(A, b)

    assert result.status == SolutionStatus.INFINITE
    assert result.particular == pytest.approx((6, 0, 0))
    assert result.rank == 1
    assert result.pivot_columns == (0,)

    assert len(result.nullspace_basis) == 2
    assert result.nullspace_basis[0] == pytest.approx(
        (-2, 1, 0)
    )
    assert result.nullspace_basis[1] == pytest.approx(
        (-3, 0, 1)
    )


def test_inconsistent_system():
    A = [[1, 2], [2, 4]]
    b = [3, 7]

    result = solve_general(A, b)

    assert result.status == SolutionStatus.INCONSISTENT
    assert result.particular is None
    assert result.rank == 1


def test_underdetermined_system():
    A = [[1, 1, 1]]
    b = [3]

    result = solve_general(A, b)

    assert result.status == SolutionStatus.INFINITE
    assert len(result.nullspace_basis) == 2


def test_overdetermined_consistent():
    A = [[1, 0], [0, 1], [1, 1]]
    b = [2, 3, 5]

    result = solve_general(A, b)

    assert result.status == SolutionStatus.UNIQUE
    assert result.particular == pytest.approx((2, 3))


def test_overdetermined_inconsistent():
    A = [[1], [1]]
    b = [2, 3]

    result = solve_general(A, b)

    assert result.status == SolutionStatus.INCONSISTENT