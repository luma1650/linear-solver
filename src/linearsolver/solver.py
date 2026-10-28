from linearsolver.types import Matrix, Vector
from linearsolver.results import SolveResult
from linearsolver.solvers.gaussian import solve_gaussian
from linearsolver.solvers.gauss_jordan import solve_gauss_jordan


def solve(
    A: Matrix,
    b: Vector,
    *,
    method: str = "gaussian",
) -> SolveResult:
    if method == "gaussian":
        solution = solve_gaussian(A, b)
    elif method == "gauss_jordan":
        solution = solve_gauss_jordan(A, b)
    else:
        raise ValueError(f"Unknown solving method: {method!r}")

    return SolveResult(
        solution=solution,
        method=method,
    )