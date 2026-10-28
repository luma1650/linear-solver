from linearsolver.types import Matrix, Vector
from linearsolver.core.rref import rref
from linearsolver.results import (
    GeneralSolveResult,
    SolutionStatus,
)


def solve_general(
    A: Matrix,
    b: Vector,
    *,
    tol: float = 1e-12,
) -> GeneralSolveResult:
    """
    Solve a general linear system Ax = b.

    Supports rectangular, singular, consistent,
    and inconsistent systems.

    Does not modify A or b.
    """
    if not A or not A[0]:
        raise ValueError("Matrix cannot be empty.")

    m = len(A)
    n = len(A[0])

    if any(len(row) != n for row in A):
        raise ValueError("Matrix must be rectangular.")

    if len(b) != m:
        raise ValueError("Incompatible dimensions.")

    augmented = [
        [*row, value]
        for row, value in zip(A, b)
    ]

    result = rref(augmented, tol=tol)

    R = result.matrix

    # Pivot columns belonging to A, excluding b.
    pivots = tuple(
        col for col in result.pivot_columns
        if col < n
    )

    rank = len(pivots)

    # A pivot in the augmented column means
    # the system is inconsistent.
    if n in result.pivot_columns:
        return GeneralSolveResult(
            status=SolutionStatus.INCONSISTENT,
            particular=None,
            nullspace_basis=(),
            rank=rank,
            pivot_columns=pivots,
        )

    # Set all free variables to zero.
    particular = [0.0] * n

    for row, col in enumerate(pivots):
        particular[col] = R[row][n]

    if rank == n:
        return GeneralSolveResult(
            status=SolutionStatus.UNIQUE,
            particular=tuple(particular),
            nullspace_basis=(),
            rank=rank,
            pivot_columns=pivots,
        )

    # Identify free columns.
    free_columns = [
        col for col in range(n)
        if col not in pivots
    ]

    basis = []

    for free_col in free_columns:
        vector = [0.0] * n
        vector[free_col] = 1.0

        for row, pivot_col in enumerate(pivots):
            vector[pivot_col] = -R[row][free_col]

        basis.append(tuple(vector))

    return GeneralSolveResult(
        status=SolutionStatus.INFINITE,
        particular=tuple(particular),
        nullspace_basis=tuple(basis),
        rank=rank,
        pivot_columns=pivots,
    )