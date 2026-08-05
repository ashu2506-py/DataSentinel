from dataclasses import dataclass
from typing import Any


@dataclass
class Rule:
    """
    Represents a validation rule loaded from YAML.
    """

    column: str
    rule_type: str
    parameters: dict[str, Any]