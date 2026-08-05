from datasentinel.anomaly.iqr import IQRDetector
from datasentinel.anomaly.zscore import ZScoreDetector


class AnomalyDetector:

    def __init__(self):

        self.detectors = {
            "zscore": ZScoreDetector(),
            "iqr": IQRDetector(),
        }

    def detect(
        self,
        dataframe,
        columns,
    ):

        results = []

        for column in columns:

            for detector in self.detectors.values():

                results.append(
                    detector.detect(
                        dataframe,
                        column,
                    )
                )

        return results