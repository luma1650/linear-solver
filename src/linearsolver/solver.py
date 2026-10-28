from collections.abc import Mapping

from linearsolver.types import Matrix, Vector, Scalar
from linearsolver.results import SolveResult, SolutionStatus
from linearsolver.exceptions import (
    InconsistentSystemError,
    InfiniteSolutionsError,
)
from linearsolver.core.constraints import apply_fixed
from linearsolver.solvers.gaussian import solve_gaussian
from linearsolver.solvers.gauss_jordan import solve_gauss_jordan
from linearsolver.solvers.general import solve_general


def solve(
    A: Matrix,
    b: Vector,
    *,
    method: str = "gaussian",
    fixed: Mapping[int, Scalar] | None = None,
) -> SolveResult:
    """
    Solve Ax = b, optionally fixing selected variables.

    Returns a unique solution or raises an exception.

    Available methods:
        gaussian
        gauss_jordan
        general
    """
    if method not in ("gaussian", "gauss_jordan", "general"):
        raise ValueError(f"Unknown solving method: {method!r}")

    if fixed is not None:
        # Validate the original system and constraints.
        if not A or not A[0]:
            raise ValueError("Matrix cannot be empty.")

        n = len(A[0])

        if any(len(row) != n for row in A):
            raise ValueError("Matrix must be rectangular.")

        if len(b) != len(A):
            raise ValueError("Incompatible dimensions.")

        A, b = apply_fixed(A, b, fixed)

    if method == "general" or fixed is not None:
        result = solve_general(A, b)

        if result.status == SolutionStatus.INCONSISTENT:
            raise InconsistentSystemError(
                "The system has no solution."
            )

        if result.status == SolutionStatus.INFINITE:
            raise InfiniteSolutionsError(
                "The system does not have a unique solution. "
                "Provide additional fixed variables."
            )

        solution = result.particular

    elif method == "gaussian":
        solution = solve_gaussian(A, b)

    else:
        solution = solve_gauss_jordan(A, b)

    assert solution is not None

    return SolveResult(
        solution=tuple(solution),
        method="general" if fixed is not None else method,
    )
