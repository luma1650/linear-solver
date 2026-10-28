from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SolveResult:
    solution: tuple[float, ...]
    method: str