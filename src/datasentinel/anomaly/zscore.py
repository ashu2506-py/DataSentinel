import numpy as np
import pandas as pd

from datasentinel.anomaly.base import BaseAnomalyDetector


class ZScoreDetector(BaseAnomalyDetector):

    def detect(
        self,
        dataframe: pd.DataFrame,
        column: str,
    ) -> dict:

        values = dataframe[column]

        mean = values.mean()
        std = values.std()

        if std == 0:
            return {
                "method": "zscore",
                "column": column,
                "outliers": [],
                "count": 0,
            }

        z_scores = np.abs((values - mean) / std)

        outliers = dataframe[z_scores > 3]

        return {
            "method": "zscore",
            "column": column,
            "count": int(len(outliers)),
            "outliers": outliers.to_dict(orient="records"),
        }