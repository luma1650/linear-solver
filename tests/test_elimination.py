import pytest

from linearsolver.core.elimination import gaussian_elimination
from linearsolver.exceptions import SingularMatrixError


def test_triangular_form():
    A = [
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2],
    ]
    b = [8, -11, -3]

    U, c = gaussian_elimination(A, b)

    n = len(U)

    for i in range(n):
        for j in range(i):
            assert U[i][j] == pytest.approx(0.0)

    assert all(U[i][i] != 0 for i in range(n))


def test_partial_pivoting():
    A = [
        [0, 1],
        [2, 3],
    ]
    b = [4, 5]

    U, c = gaussian_elimination(A, b)

    assert U == [[2.0, 3.0], [0.0, 1.0]]
    assert c == [5.0, 4.0]


def test_singular_matrix():
    A = [[1, 2], [2, 4]]
    b = [3, 6]

    with pytest.raises(SingularMatrixError):
        gaussian_elimination(A, b)


def test_input_unchanged():
    a = [[2, 1], [4, 3]]
    b = [5, 6]

    original_a = [row.copy() for row in a]
    original_b = b.copy()

    gaussian_elimination(a, b)

    assert a == original_a
    assert b == original_b


def test_immutable_input():
    a = ((2, 1), (4, 3))
    b = (5, 6)

    u, c = gaussian_elimination(a, b)

    assert len(u) == 2
    assert len(c) == 2