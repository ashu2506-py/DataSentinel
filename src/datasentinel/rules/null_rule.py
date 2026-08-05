import pandas as pd

from datasentinel.models.rule import Rule
from datasentinel.rules.base import BaseRule


class NullRule(BaseRule):

    def validate(
        self,
        dataframe: pd.DataFrame,
        rule: Rule
    ) -> dict:

        null_count = dataframe[rule.column].isnull().sum()

        return {
            "rule": "null_check",
            "column": rule.column,
            "passed": null_count == 0,
            "violations": int(null_count)
        }