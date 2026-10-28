import pytest

from linearsolver import solve, solve_gauss_jordan


@pytest.mark.parametrize(
    "A,b,expected",
    [
        ([[4]], [12], (3,)),
        ([[2, 1], [1, -1]], [5, 1], (2, 1)),
        (
            [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]],
            [8, -11, -3],
            (2, 3, -1),
        ),
    ],
)
def test_gauss_jordan(A, b, expected):
    assert solve_gauss_jordan(A, b) == pytest.approx(expected)


def test_public_api():
    result = solve(
        [[2, 1], [1, -1]],
        [5, 1],
        method="gauss_jordan",
    )

    assert result.solution == pytest.approx((2, 1))
    assert result.method == "gauss_jordan"