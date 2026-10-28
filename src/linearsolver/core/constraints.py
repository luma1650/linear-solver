from collections.abc import Mapping
from math import isfinite

from linearsolver.types import Matrix, Vector, Scalar


def apply_fixed(
    A: Matrix,
    b: Vector,
    fixed: Mapping[int, Scalar],
) -> tuple[list[list[Scalar]], list[Scalar]]:
    """Add fixed-variable constraints without modifying inputs."""
    n = len(A[0])

    constrained_A = [list(row) for row in A]
    constrained_b = list(b)

    for index, value in fixed.items():
        if type(index) is not int or not 0 <= index < n:
            raise ValueError(
                f"Invalid variable index: {index!r}"
            )

        if (
            type(value) not in (int, float)
            or not isfinite(value)
        ):
            raise ValueError(
                f"Invalid fixed value for variable {index}."
            )

        row = [0] * n
        row[index] = 1

        constrained_A.append(row)
        constrained_b.append(value)

    return constrained_A, constrained_b