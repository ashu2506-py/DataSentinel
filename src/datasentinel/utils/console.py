from rich.console import Console
from rich.table import Table

console = Console()


def show_summary(result):

    table = Table(title="DataSentinel Summary")

    table.add_column("Metric", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")

    passed = sum(
        1
        for r in result["validation"]
        if r.passed
    )

    failed = len(result["validation"]) - passed

    table.add_row("Validation Passed", str(passed))
    table.add_row("Validation Failed", str(failed))

    # Schema Drift
    schema = result["schema"]

    if isinstance(schema, dict):
        table.add_row(
            "Added Columns",
            ", ".join(schema.get("added", [])) or "None",
        )

        table.add_row(
            "Removed Columns",
            ", ".join(schema.get("removed", [])) or "None",
        )

    # Anomalies
    anomaly_count = sum(
        item.get("count", 0)
        for item in result["anomaly"]
    )

    table.add_row("Anomalies Found", str(anomaly_count))

    table.add_row("HTML Report", result["html"])
    table.add_row("PDF Report", result["pdf"])

    console.print(table)