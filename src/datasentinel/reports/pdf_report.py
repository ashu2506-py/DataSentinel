from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate


class PDFReport:

    @staticmethod
    def generate(
        validation,
        schema,
        anomaly,
        output="reports/pdf/report.pdf",
    ):

        Path(output).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        document = SimpleDocTemplate(output)

        styles = getSampleStyleSheet()

        elements = []

        elements.append(
            Paragraph(
                "<b>DataSentinel Report</b>",
                styles["Title"],
            )
        )

        elements.append(
            Paragraph(
                "<br/><b>Validation Results</b>",
                styles["Heading2"],
            )
        )

        for item in validation:

            elements.append(
                Paragraph(
                    f"""
                        Rule : {item.rule}<br/>
                        Column : {item.column}<br/>
                        Passed : {item.passed}<br/>
                        Violations : {item.violations}<br/><br/>
                        """,
                    styles["BodyText"],
                )
            )

        elements.append(
            Paragraph(
                "<br/><b>Schema Drift</b>",
                styles["Heading2"],
            )
        )

        elements.append(
            Paragraph(
                str(schema),
                styles["BodyText"],
            )
        )

        elements.append(
            Paragraph(
                "<br/><b>Anomaly Detection</b>",
                styles["Heading2"],
            )
        )

        elements.append(
            Paragraph(
                str(anomaly),
                styles["BodyText"],
            )
        )

        document.build(elements)

        return output