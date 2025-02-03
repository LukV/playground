import typer

app = typer.Typer()


@app.command()
def hello(name: str = "Luk") -> str:
    """Prints a greeting with the provided name."""
    print(f"Hello {name}")
