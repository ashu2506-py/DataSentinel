import typer

from datasentinel.engine import DataSentinelEngine

app = typer.Typer(
    help="DataSentinel - Automated Data Quality & Pipeline Monitoring Platform"
)


@app.command()
def validate(
    source_type: str,
    source_path: str,
    rules: str,
):
    engine = DataSentinelEngine()

    result = engine.run(
        source_type,
        source_path,
        rules,
    )

    typer.echo("\nValidation Completed")
    typer.echo(f"HTML Report : {result['html']}")
    typer.echo(f"PDF Report  : {result['pdf']}")


@app.command()
def report():
    """Generate report."""
    typer.echo("Report command")


@app.command()
def compare_schema():
    """Compare schemas."""
    typer.echo("Compare schema command")


@app.command()
def list_rules():
    """List rules."""
    typer.echo("List rules command")


@app.command()
def schedule():
    """Schedule validation."""
    typer.echo("Schedule command")


if __name__ == "__main__":
    app()