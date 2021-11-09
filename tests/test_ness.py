import typing as t
from unittest.mock import patch

import pytest

import ness


@pytest.mark.parametrize("format", ["parquet", "csv"])
def test_read(dl: ness.DataLake, format: str, files: t.List[str]) -> None:
    with patch("os.system") as system_mock, patch(
        "glob.glob", return_value=files
    ) as glob_mock:
        dl.read("table")

    system_mock.assert_called_once()
    glob_mock.assert_called_once()
