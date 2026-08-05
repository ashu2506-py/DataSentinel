from abc import ABC, abstractmethod

import pandas as pd


class BaseAnomalyDetector(ABC):

    @abstractmethod
    def detect(
        self,
        dataframe: pd.DataFrame,
        column: str,
    ) -> dict:
        pass