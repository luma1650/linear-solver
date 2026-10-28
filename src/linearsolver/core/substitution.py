from linearsolver.types import Matrix, Vector
from linearsolver.exceptions import SingularMatrixError


def back_substitution(
    U: Matrix,
    b: Vector,
) -> tuple[float, ...]:
    """
    Solve Ux = b for an upper triangular matrix U.

    Assumes U is square, upper triangular and has
    dimensions compatible with b.
    Does not modify the inputs.
    """
    n = len(U)
    x = [0.0] * n

    for i in range(n - 1, -1, -1):
        pivot = U[i][i]

        if pivot == 0:
            raise SingularMatrixError(
                f"Zero diagonal entry at row {i}."
            )

        total = sum(
            U[i][j] * x[j]
            for j in range(i + 1, n)
        )

        x[i] = (b[i] - total) / pivot

    return tuple(x)