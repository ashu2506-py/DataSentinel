class DriftDetector:

    def compare(
        self,
        old_schema: dict,
        new_schema: dict,
    ):

        old_columns = set(old_schema.keys())
        new_columns = set(new_schema.keys())

        added = list(new_columns - old_columns)

        removed = list(old_columns - new_columns)

        changed = []

        for column in old_columns.intersection(new_columns):

            if old_schema[column] != new_schema[column]:

                changed.append(
                    {
                        "column": column,
                        "old": old_schema[column],
                        "new": new_schema[column],
                    }
                )

        return {
            "added": added,
            "removed": removed,
            "changed": changed,
        }