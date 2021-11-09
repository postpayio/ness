import glob
import typing as t

import pytest
from click.testing import CliRunner

import ness


@pytest.fixture
def dl(format: str) -> ness.datalake.DataLake:
    return ness.dl(bucket="bucket", key="key", format=format)


@pytest.fixture
def files(format: str) -> t.List[str]:
    return glob.glob(f"tests/data/table.{format}/*")


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()
