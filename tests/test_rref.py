import pytest

from linearsolver.core.rref import rref


def assert_matrix_approx(actual, expected):
    assert len(actual) == len(expected)

    for row, expected_row in zip(actual, expected):
        assert row == pytest.approx(expected_row)


def test_invertible_matrix():
    result = rref([[2, 1], [1, -1]])

    assert_matrix_approx(
        result.matrix,
        [[1, 0], [0, 1]],
    )
    assert result.pivot_columns == (0, 1)
    assert result.rank == 2


def test_rank_deficient():
    result = rref([[1, 2, 3], [2, 4, 6]])

    assert_matrix_approx(
        result.matrix,
        [[1, 2, 3], [0, 0, 0]],
    )
    assert result.pivot_columns == (0,)
    assert result.rank == 1


def test_skipped_pivot_column():
    result = rref([[0, 1, 2], [0, 0, 3]])

    assert_matrix_approx(
        result.matrix,
        [[0, 1, 0], [0, 0, 1]],
    )
    assert result.pivot_columns == (1, 2)


def test_zero_matrix():
    result = rref([[0, 0], [0, 0]])

    assert result.rank == 0
    assert result.pivot_columns == ()


def test_inputs_unchanged():
    A = [[1, 2], [2, 4]]
    original = [row.copy() for row in A]

    rref(A)

    assert A == original