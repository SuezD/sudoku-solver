from dataclasses import dataclass

@dataclass
class Step:
    row: int
    col: int
    value: int
    technique: str
    explanation: str
