import glob
import os
import typing as t
from pathlib import Path

import pandas as pd


class DataLake:
    def __init__(
        self,
        bucket: str,
        key: str,
        format: str = None,
        profile: str = None,
    ) -> None:
        self.bucket = bucket
        self.key = key
        self.format = format or "parquet"
        self.profile = profile

    def read(self, table: str, sync: bool = False, **kwargs: t.Any) -> pd.DataFrame:
        path = Path.home() / f".ness/{self.key}/{table}.{self.format}"

        if sync or not os.path.isdir(path) or not os.listdir(path):
            self.sync(table)

        reader = getattr(pd, f"read_{self.format}", pd.read_parquet)
        return pd.concat(map(lambda f: reader(f, **kwargs), glob.glob(f"{path}/*")))

    def sync(self, table: str = None) -> None:
        cmd = (
            f"aws s3 sync s3://{self.bucket}/{self.key} ~/.ness/{self.key} "
            f"--exclude '*' --include '*{table or ''}.{self.format}*' --delete"
        )

        if self.profile is not None:
            cmd += f" --profile {self.profile}"

        os.system(cmd)
