import glob
import os
import typing as t
from pathlib import Path

import pandas as pd


class DataLake:
    def __init__(self, bucket: str, key: str, format: str = None) -> None:
        self.bucket = bucket
        self.key = key
        self.format = format or "parquet"

    def read(self, table: str, **kwargs: t.Any) -> pd.DataFrame:
        if self.format == "csv":
            reader = pd.read_csv
        else:
            reader = pd.read_parquet

        path = f"{Path.home()}/.ness/{self.key}/{table}.{self.format}"

        if not os.path.isdir(path) or not os.listdir(path):
            self.sync(table)

        return pd.concat(map(lambda f: reader(f, **kwargs), glob.glob(f"{path}/*")))

    def sync(self, table: str = None) -> None:
        os.system(
            f"aws s3 sync s3://{self.bucket}/{self.key} ~/.ness/{self.key}"
            f" --exclude '*' --include '*{table or self.format}*'"
        )
