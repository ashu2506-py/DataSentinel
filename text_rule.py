import pandas as pd

from datasentinel.schema.fingerprint import SchemaFingerprint
from datasentinel.schema.drift_detector import DriftDetector

baseline = pd.DataFrame(
    {
        "id": [1],
        "name": ["Alice"],
        "age": [25],
    }
)

current = pd.DataFrame(
    {
        "id": [1],
        "name": ["Alice"],
        "salary": [50000],
    }
)

fingerprint = SchemaFingerprint()

baseline_schema = fingerprint.generate(baseline)

fingerprint.save(baseline_schema)

old = fingerprint.load()

current_schema = fingerprint.generate(current)

detector = DriftDetector()

result = detector.compare(
    old,
    current_schema,
)

print(result)