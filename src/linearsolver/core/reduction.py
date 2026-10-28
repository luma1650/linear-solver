from linearsolver.types import Matrix, Vector
from linearsolver.core.elimination import gaussian_elimination


def gauss_jordan_reduction(
    A: Matrix,
    b: Vector,
) -> tuple[list[list[float]], list[float]]:
    """
    Reduce a nonsingular square system Ax = b to [I | x]
    using Gaussian elimination followed by backward reduction.

    Assumes validated inputs.
    Does not mutate A or b.
    """
    U, c = gaussian_elimination(A, b)
    n = len(U)

    for k in range(n - 1, -1, -1):
        pivot = U[k][k]

        # Normalize pivot row.
        for j in range(k, n):
            U[k][j] /= pivot

        c[k] /= pivot

        # Eliminate entries above the pivot.
        for i in range(k):
            factor = U[i][k]

            for j in range(k, n):
                U[i][j] -= factor * U[k][j]

            c[i] -= factor * c[k]

            U[i][k] = 0.0

        U[k][k] = 1.0

    return U, c