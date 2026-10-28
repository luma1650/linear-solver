import pytest

from linearsolver.core.reduction import gauss_jordan_reduction
from linearsolver.exceptions import SingularMatrixError


def test_identity_reduction():
    A = [[2, 1], [1, -1]]
    b = [5, 1]

    R, c = gauss_jordan_reduction(A, b)

    for row, expected in zip(R, [[1, 0], [0, 1]]):
        assert row == pytest.approx(expected)
    assert c == pytest.approx((2, 1))


def test_3x3_reduction():
    A = [
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2],
    ]
    b = [8, -11, -3]

    R, c = gauss_jordan_reduction(A, b)

    for i in range(3):
        for j in range(3):
            expected = 1.0 if i == j else 0.0
            assert R[i][j] == pytest.approx(expected)

    assert c == pytest.approx((2, 3, -1))


def test_singular_matrix():
    A = [[1, 2], [2, 4]]
    b = [3, 6]

    with pytest.raises(SingularMatrixError):
        gauss_jordan_reduction(A, b)


def test_inputs_unchanged():
    A = [[2, 1], [1, -1]]
    b = [5, 1]

    original_A = [row.copy() for row in A]
    original_b = b.copy()

    gauss_jordan_reduction(A, b)

    assert A == original_A
    assert b == original_b