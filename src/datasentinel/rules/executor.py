from datasentinel.rules.null_rule import NullRule
from datasentinel.rules.unique_rule import UniqueRule
from datasentinel.rules.range_rule import RangeRule
from datasentinel.rules.regex_rule import RegexRule
from datasentinel.rules.foreign_key_rule import ForeignKeyRule


class RuleExecutor:

    def __init__(self):

        self.validators = {
            "null_check": NullRule(),
            "unique_check": UniqueRule(),
            "range": RangeRule(),
            "regex": RegexRule(),
            "foreign_key": ForeignKeyRule(),
        }

    def execute(
            self,
            dataframe,
            rules,
        ):

            results = []

            for rule in rules:

                if rule.column not in dataframe.columns:

                    results.append(
                        {
                            "rule": rule.rule_type,
                            "column": rule.column,
                            "passed": False,
                            "violations": 0,
                            "error": f"Column '{rule.column}' not found."
                        }
                    )

                    continue

                validator = self.validators[rule.rule_type]

                results.append(
                    validator.validate(
                        dataframe,
                        rule,
                    )
                )

            return results