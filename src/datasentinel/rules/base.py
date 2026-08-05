from abc import ABC, abstractmethod

import pandas as pd

from datasentinel.models.rule import Rule


class BaseRule(ABC):

    @abstractmethod
    def validate(
        self,
        dataframe: pd.DataFrame,
        rule: Rule
    ) -> dict:
        pass