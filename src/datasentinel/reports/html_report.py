from pathlib import Path

from jinja2 import Environment
from jinja2 import FileSystemLoader
from dataclasses import asdict

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

        html = template.render(
            validation=validation,
            schema=schema,
            anomaly=anomaly,
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