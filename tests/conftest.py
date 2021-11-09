import glob
import typing as t

import pytest

import ness


@pytest.fixture
def dl(format: str) -> ness.datalake.DataLake:
    return ness.dl(bucket="ness", key="test", format=format)


@pytest.fixture
def files(format: str) -> t.List[str]:
    return glob.glob(f"tests/data/table.{format}/*")
