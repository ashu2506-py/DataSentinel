import pandas as pd

from datasentinel.models.rule import Rule
from datasentinel.rules.executor import RuleExecutor


df = pd.DataFrame(
    {
        "id": [1, 2, 2, 4],
        "name": ["Alice", None, "Charlie", "David"],
        "age": [25, 150, 30, 15],
        "email": [
            "alice@gmail.com",
            "wrong-email",
            "charlie@gmail.com",
            "david@gmail.com",
        ],
    }
)

rules = [

    Rule(
        column="name",
        rule_type="null_check",
        parameters={}
    ),

    Rule(
        column="id",
        rule_type="unique_check",
        parameters={}
    ),

    Rule(
        column="age",
        rule_type="range",
        parameters={
            "min":18,
            "max":60,
        }
    ),

    Rule(
        column="email",
        rule_type="regex",
        parameters={
            "pattern":r"^[\w\.-]+@[\w\.-]+\.\w+$"
        }
    ),
]

executor = RuleExecutor()

results = executor.execute(
    df,
    rules,
)

for result in results:
    print(result)