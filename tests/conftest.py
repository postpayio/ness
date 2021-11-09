import glob
import typing as t

import pytest

import ness


@pytest.fixture
def dl(format: str) -> ness.DataLake:
    return ness.dl(bucket="ness", name="test", format=format)


@pytest.fixture
def files(format: str) -> t.List[str]:
    return glob.glob(f"tests/data/table.{format}/*")
