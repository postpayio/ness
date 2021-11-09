from unittest.mock import patch

from click.testing import CliRunner

from ness.cli import main


def test_sync(runner: CliRunner) -> None:
    with patch("os.system") as system_mock:
        result = runner.invoke(main, ["sync", "bucket/key"])

    assert result.exit_code == 0
    system_mock.assert_called_once()
