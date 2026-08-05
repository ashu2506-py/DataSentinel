import pandas as pd

from datasentinel.rules.loader import RuleLoader
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

rules = RuleLoader.load(
    "configs/rules.yaml"
)

executor = RuleExecutor()

results = executor.execute(
    df,
    rules,
)

for result in results:
    print(result)