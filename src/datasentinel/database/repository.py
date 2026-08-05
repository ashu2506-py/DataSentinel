import json

from datasentinel.database.database import SessionLocal
from datasentinel.database.models import ValidationRun


class ValidationRepository:

    def __init__(self):
        self.session = SessionLocal()

    def save(
        
        self,
        dataset,
        validation,
        schema,
        anomaly,
        html,
        pdf,
    ):
        print("Saving validation run to database...")
        # Convert to plain JSON-compatible Python objects
        validation = json.loads(json.dumps(validation))
        schema = json.loads(json.dumps(schema))
        anomaly = json.loads(json.dumps(anomaly))

        run = ValidationRun(
            dataset=dataset,
            validation=validation,
            schema=schema,
            anomaly=anomaly,
            html_report=html,
            pdf_report=pdf,
        )

        self.session.add(run)
        self.session.commit()
        print("Saved successfully!")

        return run.id