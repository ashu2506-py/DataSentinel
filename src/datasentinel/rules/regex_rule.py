import pandas as pd

from datasentinel.models.rule import Rule
from datasentinel.rules.base import BaseRule


class RegexRule(BaseRule):

    def validate(
        self,
        dataframe: pd.DataFrame,
        rule: Rule
    ) -> dict:

        pattern = rule.parameters["pattern"]

        valid = dataframe[rule.column].astype(str).str.match(pattern)

        invalid = (~valid).sum()

        return {
            "rule": "regex_check",
            "column": rule.column,
            "passed": invalid == 0,
            "violations": int(invalid)
        }