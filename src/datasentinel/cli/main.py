import typer
from rich.console import Console

app = typer.Typer(
    help="DataSentinel - Automated Data Quality & Pipeline Monitoring Platform"
)

console = Console()


@app.callback()
def main():
    """
    DataSentinel CLI
    """
    pass


@app.command()
def hello():
    """
    Display a welcome message.
    """
    console.print(
        "[bold green]Welcome to DataSentinel![/bold green]"
    )