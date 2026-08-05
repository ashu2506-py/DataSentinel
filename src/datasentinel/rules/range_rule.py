import pandas as pd

from datasentinel.models.rule import Rule
from datasentinel.rules.base import BaseRule


class RangeRule(BaseRule):

    def validate(
        self,
        dataframe: pd.DataFrame,
        rule: Rule
    ) -> dict:

        minimum = rule.parameters["min"]
        maximum = rule.parameters["max"]

        invalid_rows = dataframe[
            (dataframe[rule.column] < minimum)
            | (dataframe[rule.column] > maximum)
        ]

        return {
            "rule": "range_check",
            "column": rule.column,
            "passed": invalid_rows.empty,
            "violations": len(invalid_rows)
        }