from dataclasses import dataclass

from linearsolver.types import Matrix


@dataclass(frozen=True, slots=True)
class RREFResult:
    matrix: tuple[tuple[float, ...], ...]
    pivot_columns: tuple[int, ...]
    rank: int


def rref(A: Matrix, *, tol: float = 1e-12) -> RREFResult:
    """
    Compute the reduced row echelon form of a matrix.

    Supports rectangular and rank-deficient matrices.
    Does not modify the input.
    """
    if not A:
        raise ValueError("Matrix cannot be empty.")

    m = len(A)
    n = len(A[0])

    if n == 0 or any(len(row) != n for row in A):
        raise ValueError("Matrix must be nonempty and rectangular.")

    M = [[float(x) for x in row] for row in A]

    pivot_row = 0
    pivot_columns = []

    for col in range(n):
        if pivot_row >= m:
            break

        best = max(
            range(pivot_row, m),
            key=lambda i: abs(M[i][col]),
        )

        if abs(M[best][col]) <= tol:
            continue

        M[pivot_row], M[best] = M[best], M[pivot_row]

        pivot = M[pivot_row][col]

        for j in range(col, n):
            M[pivot_row][j] /= pivot

        M[pivot_row][col] = 1.0

        for i in range(m):
            if i == pivot_row:
                continue

            factor = M[i][col]

            for j in range(col, n):
                M[i][j] -= factor * M[pivot_row][j]

            M[i][col] = 0.0

        pivot_columns.append(col)
        pivot_row += 1

    return RREFResult(
        matrix=tuple(tuple(row) for row in M),
        pivot_columns=tuple(pivot_columns),
        rank=len(pivot_columns),
    )