import pandas as pd
import click

from analyse_903_tool.utils import read_data, ingress, gender_count, child_count

# Add command line functionality with CLICK
@click.command()
@click.argument("filepath", required=True)

def run_app(filepath):
    # TODO write docstring
    # filepath = 'https://raw.githubusercontent.com/data-to-insight/csc-validator-be-903/main/tests/fake_data/header.csv'
    df = read_data(filepath)
    df_ingressed = ingress(df)

    male, female = gender_count(df_ingressed)
    counts = child_count(df_ingressed)

    click.echo(f'Total children: {counts}')
    click.echo(f'Total male: {male}')
    click.echo(f'Total female: {female}')

if __name__ == "__main__":
    run_app()