import pandas as pd

from datasentinel.models.rule import Rule
from datasentinel.rules.null_rule import NullRule


df = pd.DataFrame(
    {
        "name": ["Alice", "Bob", None, "David"],
        "age": [20, 21, 22, 23],
    }
)

rule = Rule(
    column="name",
    rule_type="null_check",
    parameters={}
)

validator = NullRule()

result = validator.validate(df, rule)

print(result)