import pandas as pd

from datasentinel.models.rule import Rule
from datasentinel.rules.base import BaseRule
from datasentinel.models.result import ValidationResult

class UniqueRule(BaseRule):

    def validate(
        self,
        dataframe: pd.DataFrame,
        rule: Rule
    ) -> dict:

        duplicate_count = dataframe.duplicated(
            subset=[rule.column]
        ).sum()

        return ValidationResult(
            rule="unique_check",
            column=rule.column,
            passed=(duplicate_count == 0),
            violations=int(duplicate_count),
        )