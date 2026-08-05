import json
from pathlib import Path

import pandas as pd


class SchemaFingerprint:

    def __init__(self):
        self.baseline_path = Path("configs/schema_baseline.json")

    def generate(self, dataframe: pd.DataFrame) -> dict:

        schema = {}

        for column in dataframe.columns:
            schema[column] = str(dataframe[column].dtype)

        return schema

    def save(self, schema: dict):

        with open(self.baseline_path, "w") as file:
            json.dump(schema, file, indent=4)

    def load(self):

        if not self.baseline_path.exists():
            return None

        with open(self.baseline_path, "r") as file:
            return json.load(file)