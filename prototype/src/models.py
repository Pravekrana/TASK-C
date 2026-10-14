from dataclasses import dataclass

@dataclass(frozen=True)
class Stock:
    id: str
    project: str
    grade: str
    section: str
    length_mm: int
    kg_per_m: float
    kind: str

@dataclass(frozen=True)
class Demand:
    id: str
    project: str
    grade: str
    section: str
    length_mm: int
    quantity: int
