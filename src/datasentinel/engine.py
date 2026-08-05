import pandas as pd

from datasentinel.connectors.factory import ConnectorFactory
from datasentinel.rules.loader import RuleLoader
from datasentinel.rules.executor import RuleExecutor
from datasentinel.schema.fingerprint import SchemaFingerprint
from datasentinel.schema.drift_detector import DriftDetector
from datasentinel.anomaly.detector import AnomalyDetector
from datasentinel.reports.html_report import HTMLReport
from datasentinel.reports.pdf_report import PDFReport
from datasentinel.database.repository import ValidationRepository
from datasentinel.alerts.email_alert import EmailSender
from dataclasses import asdict
from dotenv import load_dotenv

load_dotenv()
class DataSentinelEngine:

    def __init__(self):
        
        self.rule_loader = RuleLoader()
        self.rule_executor = RuleExecutor()

        self.fingerprint = SchemaFingerprint()
        self.drift = DriftDetector()

        self.anomaly = AnomalyDetector()

        self.html = HTMLReport()

        self.pdf = PDFReport()
        self.repository = ValidationRepository()
        self.email = EmailSender()

    def run(
        self,
        source_type: str,
        source_path: str,
        rule_file: str,
    ):

        connector = ConnectorFactory.create(
            source_type,
            source_path,
        )

        connector.connect()

        dataframe = connector.load()

        connector.disconnect()

        rules = self.rule_loader.load(rule_file)

        validation = self.rule_executor.execute(
            dataframe,
            rules,
        )

        current_schema = self.fingerprint.generate(
            dataframe
        )

        baseline = self.fingerprint.load()

        if baseline is None:

            self.fingerprint.save(current_schema)

            schema_result = {
                "message": "Baseline created."
            }

        else:

            schema_result = self.drift.compare(
                baseline,
                current_schema,
            )

        numeric_columns = dataframe.select_dtypes(
            include="number"
        ).columns.tolist()

        anomaly_result = self.anomaly.detect(
            dataframe,
            numeric_columns,
        )

        html = self.html.generate(
            validation,
            schema_result,
            anomaly_result,
        )

        pdf = self.pdf.generate(
            validation,
            schema_result,
            anomaly_result,
        )
        
        validation_json = [v.to_dict() for v in validation]

        self.repository.save(

            source_path,

            validation_json,

            schema_result,

            anomaly_result,

            html,

            pdf,

        )
        self.email.send(
            receiver="codewithcodex2106@gmail.com",
            subject="DataSentinel Validation Report",
            body="Validation completed successfully. Please find the attached PDF report.",
            attachment=pdf,
        )

        return {
            "validation": validation,
            "schema": schema_result,
            "anomaly": anomaly_result,
            "html": html,
            "pdf": pdf,
        }