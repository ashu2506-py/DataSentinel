import pandas as pd

from datasentinel.anomaly.detector import AnomalyDetector


df = pd.DataFrame(
    {
        "salary": [
            45000,
            47000,
            49000,
            51000,
            53000,
            55000,
            900000,
        ],
        "age": [
            20,
            21,
            22,
            23,
            24,
            25,
            120,
        ],
    }
)

detector = AnomalyDetector()

results = detector.detect(
    df,
    ["salary", "age"],
)

for result in results:
    print(result)