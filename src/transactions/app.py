import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """An app to store and serve my personal transactions."""
    click.echo("Hello, world!")
