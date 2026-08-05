import pandas as pd

from datasentinel.models.rule import Rule
from datasentinel.rules.base import BaseRule


class UniqueRule(BaseRule):

    def validate(
        self,
        dataframe: pd.DataFrame,
        rule: Rule
    ) -> dict:

        duplicate_count = dataframe.duplicated(
            subset=[rule.column]
        ).sum()

        return {
            "rule": "unique_check",
            "column": rule.column,
            "passed": duplicate_count == 0,
            "violations": int(duplicate_count)
        }