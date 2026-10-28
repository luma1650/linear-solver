import pytest

from linearsolver.core.validation import validate_system
from linearsolver.exceptions import (
    DimensionError, ValidationError,
)


def test_valid_system():
    A = [[2, 1], [3, 4]]
    b = [5, 6]

    assert validate_system(A, b) == (2, 2)


def test_empty_matrix():
    with pytest.raises(ValidationError):
        validate_system([], [])


def test_ragged_matrix():
    with pytest.raises(ValidationError):
        validate_system([[1, 2], [3]], [4, 5])


def test_dimension_mismatch():
    with pytest.raises(DimensionError):
        validate_system([[1, 2], [3, 4]], [5])


def test_nonsquare_matrix():
    with pytest.raises(DimensionError):
        validate_system([[1, 2, 3], [4, 5, 6]], [7, 8])


@pytest.mark.parametrize("value", [float("nan"), float("inf"), -float("inf")])
def test_nonfinite_coefficients(value):
    with pytest.raises(ValidationError):
        validate_system([[1, value], [3, 4]], [5, 6])


def test_immutable_sequences():
    A = ((1, 2), (3, 4))
    b = (5, 6)

    assert validate_system(A, b) == (2, 2)