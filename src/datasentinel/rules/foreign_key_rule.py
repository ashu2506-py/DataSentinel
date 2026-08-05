import pandas as pd

from datasentinel.models.rule import Rule
from datasentinel.rules.base import BaseRule


class ForeignKeyRule(BaseRule):

    def validate(
        self,
        dataframe: pd.DataFrame,
        rule: Rule
    ) -> dict:

        reference = rule.parameters["reference"]

        invalid = ~dataframe[rule.column].isin(reference)

        return {
            "rule": "foreign_key",
            "column": rule.column,
            "passed": invalid.sum() == 0,
            "violations": int(invalid.sum())
        }