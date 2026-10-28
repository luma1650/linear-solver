"""Tipos compartidos para sistemas lineales con coeficientes reales.

Las entradas aceptan secuencias; los algoritmos deben copiarlas antes de
modificarlas. Los tipos no comprueban dimensiones ni valores en ejecución.
"""

from collections.abc import Sequence
from typing import TypeAlias

Scalar: TypeAlias = int | float
Vector: TypeAlias = Sequence[Scalar]
Matrix: TypeAlias = Sequence[Sequence[Scalar]]

# Representaciones mutables para los cálculos internos.
MutableVector: TypeAlias = list[float]
MutableMatrix: TypeAlias = list[list[float]]

__all__ = ["Scalar", "Vector", "Matrix", "MutableVector", "MutableMatrix"]
