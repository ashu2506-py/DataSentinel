import pandas as pd

from datasentinel.anomaly.base import BaseAnomalyDetector


class IQRDetector(BaseAnomalyDetector):

    def detect(
        self,
        dataframe: pd.DataFrame,
        column: str,
    ) -> dict:

        q1 = dataframe[column].quantile(0.25)
        q3 = dataframe[column].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - (1.5 * iqr)
        upper = q3 + (1.5 * iqr)

        outliers = dataframe[
            (dataframe[column] < lower)
            | (dataframe[column] > upper)
        ]

        return {
            "method": "iqr",
            "column": column,
            "count": len(outliers),
            "outliers": outliers.to_dict(orient="records"),
        }