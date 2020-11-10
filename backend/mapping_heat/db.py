import sqlite3

import click
import csv
import csv_to_sqlite
import os
from flask import current_app, g
from flask.cli import with_appcontext


def init_db():
    currentDir = os.getcwd()
    dataPath = currentDir + "/mapping_heat/fixtures/pitching_data.csv"
    instance_path = currentDir + "/instance/mapping_heat.sqlite"
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
        # df = pandas.read_csv(dataPath)
        # df.to_sql(df.to_sql("pitching_data", con=db, if_exists='replace', index=False))
        options = csv_to_sqlite.CsvOptions(typing_style="full", delimiter=",", drop_tables=True)
        csv_to_sqlite.write_csv([dataPath], instance_path, options)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database')