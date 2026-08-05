from dataclasses import dataclass
from typing import Any


@dataclass
class ValidationResult:

    rule: str

    column: str

    passed: bool

    violations: int

    details: Any = None