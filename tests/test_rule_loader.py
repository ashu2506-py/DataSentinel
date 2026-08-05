from pathlib import Path

from datasentinel.rules.loader import RuleLoader


def test_rule_loader():

    rule_file = Path("configs/rules.yaml")

    loader = RuleLoader()

    rules = loader.load(str(rule_file))

    assert rules is not None
    assert isinstance(rules, list)
    assert len(rules) > 0