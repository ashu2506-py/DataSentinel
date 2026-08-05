from pathlib import Path
from dataclasses import asdict
from datetime import datetime

from jinja2 import Environment, FileSystemLoader


class HTMLReport:

    def __init__(self):

        template_dir = Path(
            "src/datasentinel/reports/templates"
        )

        self.environment = Environment(
            loader=FileSystemLoader(template_dir)
        )

    def generate(
        self,
        validation,
        schema,
        anomaly,
        output="reports/html/report.html",
    ):

        template = self.environment.get_template(
            "report.html"
        )

        validation = [
            asdict(item)
            for item in validation
        ]

        total_rules = len(validation)

        passed_rules = sum(
            1
            for item in validation
            if item["passed"]
        )

        failed_rules = total_rules - passed_rules

        total_anomalies = sum(
            item.get("count", 0)
            for item in anomaly
        )

        html = template.render(

            validation=validation,

            schema=schema,

            anomaly=anomaly,

            total_rules=total_rules,

            passed_rules=passed_rules,

            failed_rules=failed_rules,

            total_anomalies=total_anomalies,

            generated_at=datetime.now().strftime(
                "%d %b %Y %I:%M %p"
            ),
        )

        Path(output).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(
            output,
            "w",
            encoding="utf-8",
        ) as file:

            file.write(html)

        return output