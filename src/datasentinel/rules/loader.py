import yaml

from datasentinel.models.rule import Rule


class RuleLoader:

    @staticmethod
    def load(file_path: str) -> list[Rule]:

        with open(file_path, "r") as file:
            config = yaml.safe_load(file)

        rules = []

        for item in config["rules"]:

            parameters = {
                key: value
                for key, value in item.items()
                if key not in ("column", "type")
            }

            rules.append(
                Rule(
                    column=item["column"],
                    rule_type=item["type"],
                    parameters=parameters,
                )
            )

        return rules