from dataclasses import dataclass
from enum import Enum, auto


class SolutionStatus(Enum):
    UNIQUE = auto()
    INFINITE = auto()
    INCONSISTENT = auto()


@dataclass(frozen=True, slots=True)
class SolveResult:
    solution: tuple[float, ...]
    method: str


@dataclass(frozen=True, slots=True)
class GeneralSolveResult:
    status: SolutionStatus
    particular: tuple[float, ...] | None
    nullspace_basis: tuple[tuple[float, ...], ...]
    rank: int
    pivot_columns: tuple[int, ...]