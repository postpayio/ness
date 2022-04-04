import click

from .datalake import DataLake


@click.group()
def main() -> None:
    """Ness cli"""


@main.command()
@click.argument("s3_uri")
@click.option("--format", default="parquet", help="Data lake source format.")
@click.option("--profile", help="AWS profile.")
@click.option("--table", help="Table name to sync.")
def sync(s3_uri: str, format: str, profile: str = None, table: str = None) -> None:
    bucket, key = s3_uri.split("/", 1)
    dl = DataLake(bucket, key, format=format, profile=profile)
    dl.sync(table)
