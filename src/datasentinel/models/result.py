from dataclasses import dataclass
from typing import Any


@dataclass
class ValidationResult:
    rule: str
    column: str
    passed: bool
    violations: int
    details: Any = None

    def to_dict(self):
        return {
            "rule": self.rule,
            "column": self.column,
            "passed": bool(self.passed),
            "violations": int(self.violations),
            "details": self.details,
        }