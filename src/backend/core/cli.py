"""CLI interface for the core module."""

from collections.abc import Iterable

import typer

app = typer.Typer()


@app.command()
def hello(name: str = "Luk") -> str:
    """Print a greeting with the provided name."""
    print(f"Hello {name}")


def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Sum all even numbers in the provided iterable."""
    return sum(num for num in numbers if num % 2 == 0)
