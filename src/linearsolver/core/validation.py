from math import isfinite

from linearsolver.exceptions import (
    ValidationError,
    DimensionError,
)
from linearsolver.types import Matrix, Vector


def validate_system(
    A: Matrix,
    b: Vector,
) -> tuple[int, int]:
    """Validate Ax = b and return matrix dimensions."""

    if not A:
        raise ValidationError("Matrix cannot be empty.")

    rows = len(A)
    cols = len(A[0])

    if cols == 0:
        raise ValidationError("Matrix rows cannot be empty.")

    for row in A:
        if len(row) != cols:
            raise ValidationError("Matrix must be rectangular.")

        for value in row:
            if type(value) not in (int, float):
                raise ValidationError(
                    "Matrix entries must be real numbers."
                )

            if not isfinite(value):
                raise ValidationError(
                    "Matrix entries must be finite."
                )

    if len(b) != rows:
        raise DimensionError(
            f"Expected {rows} values in b, got {len(b)}."
        )

    for value in b:
        if type(value) not in (int, float) or not isfinite(value):
            raise ValidationError(
                "Vector entries must be finite real numbers."
            )

    if rows != cols:
        raise DimensionError(
            "The initial solver requires a square matrix."
        )

    return rows, cols