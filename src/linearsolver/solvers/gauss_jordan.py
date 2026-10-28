from linearsolver.types import Matrix, Vector
from linearsolver.core.validation import validate_system
from linearsolver.core.reduction import gauss_jordan_reduction


def solve_gauss_jordan(
    A: Matrix,
    b: Vector,
) -> tuple[float, ...]:
    """
    Solve Ax = b using Gauss-Jordan elimination.

    Requires a square, nonsingular matrix.
    Does not mutate the inputs.
    """
    validate_system(A, b)

    _, c = gauss_jordan_reduction(A, b)

    return tuple(c)