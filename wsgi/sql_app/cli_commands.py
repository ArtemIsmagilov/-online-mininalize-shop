import click
from flask import current_app

from .databse import Base, engine


def init_app(app: current_app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(drop_db_command)


@click.command("init-db")
def init_db_command():
    "Run initialize database"
    Base.metadata.create_all(engine)
    click.echo("Initialized the database.")


@click.command("drop-db")
def drop_db_command():
    "Run drop database"
    Base.metadata.drop_all(engine)
    click.echo("Dropped the database.")
