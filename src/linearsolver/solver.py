from linearsolver.types import Matrix, Vector
from linearsolver.results import SolveResult
from linearsolver.solvers.gaussian import solve_gaussian


def solve(
    A: Matrix,
    b: Vector,
    *,
    method: str = "gaussian",
) -> SolveResult:
    if method == "gaussian":
        solution = solve_gaussian(A, b)
    else:
        raise ValueError(f"Unknown solving method: {method!r}")

    return SolveResult(
        solution=solution,
        method=method,
    )