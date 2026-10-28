from linearsolver.types import Matrix, Vector
from linearsolver.core.validation import validate_system
from linearsolver.core.elimination import gaussian_elimination
from linearsolver.core.substitution import back_substitution


def solve_gaussian(
    A: Matrix,
    b: Vector,
) -> tuple[float, ...]:
    """
    Solve Ax = b using Gaussian elimination
    with partial pivoting.

    Requires a square, nonsingular matrix.
    Does not mutate the inputs.
    """
    validate_system(A, b)

    U, c = gaussian_elimination(A, b)

    return back_substitution(U, c)