"""Jerarquía de errores del paquete LinearSolver."""


class LinearSolverError(Exception):
    """Error base de la biblioteca."""


class ValidationError(LinearSolverError, ValueError):
    """Los datos o parámetros de entrada no son válidos."""


class DimensionError(ValidationError):
    """Las dimensiones de la matriz y del vector son incompatibles."""


class NumericalError(LinearSolverError, ArithmeticError):
    """El cálculo no puede continuar de forma numéricamente válida."""


class SingularMatrixError(NumericalError):
    """La matriz es singular y no permite obtener una solución única."""


class InconsistentSystemError(SingularMatrixError):
    """El sistema es incompatible: no tiene solución."""


class InfiniteSolutionsError(SingularMatrixError):
    """El sistema es indeterminado: tiene infinitas soluciones."""


__all__ = [
    "LinearSolverError",
    "ValidationError",
    "DimensionError",
    "NumericalError",
    "SingularMatrixError",
    "InconsistentSystemError",
    "InfiniteSolutionsError",
]
