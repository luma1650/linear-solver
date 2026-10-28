from linearsolver.types import Matrix, Vector
from linearsolver.exceptions import SingularMatrixError


def gaussian_elimination(
    a: Matrix,
    b: Vector,
) -> tuple[list[list[float]], list[float]]:
    """
    Perform Gaussian elimination with partial pivoting.

    Assumes A is a validated square matrix and len(b) == len(A).
    Does not mutate the input arguments.
    """
    n = len(a)

    u = [[float(value) for value in row] for row in a]
    c = [float(value) for value in b]

    for k in range(n):
        # Choose row with largest absolute pivot.
        pivot_row = max(
            range(k, n),
            key=lambda x: abs(u[x][k]),
        )

        if u[pivot_row][k] == 0.0:
            raise SingularMatrixError(
                f"Zero pivot encountered at column {k}."
            )

        if pivot_row != k:
            u[k], u[pivot_row] = u[pivot_row], u[k]
            c[k], c[pivot_row] = c[pivot_row], c[k]

        pivot = u[k][k]

        # Eliminate entries below the pivot.
        for i in range(k + 1, n):
            factor = u[i][k] / pivot
            u[i][k] = 0.0

            for j in range(k + 1, n):
                u[i][j] -= factor * u[k][j]

            c[i] -= factor * c[k]

    return u, c