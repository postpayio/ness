# Ness

<p align="center">
    <em>A Python datalake client.</em>
</p>
<p align="center">
    <a href="https://github.com/postpayio/ness/actions">
        <img src="https://github.com/postpayio/ness/actions/workflows/test-suite.yml/badge.svg" alt="Test">
    </a>
    <a href="https://codecov.io/gh/postpayio/ness">
        <img src="https://img.shields.io/codecov/c/github/postpayio/ness?color=%2334D058" alt="Coverage">
    </a>
    <a href="https://pypi.org/project/ness">
        <img src="https://img.shields.io/pypi/v/ness" alt="Package version">
    </a>
</p>

## Requirements

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

## Installation

```sh
pip install pyarrow ness
```

## Quickstart

```py
import ness

dl = ness.dl(bucket="mybucket", key="mydatalake")
df = dl.read("mytable")
```

## Sync

```py
# Sync all tables
dl.sync()

# Sync a single table
dl.sync("mytable")

# Sync and read a single table
df = dl.read("mytable", sync=True)
```

## Format

Specify the input data source format, the default format is `parquet`:

```py
import ness

dl = ness.dl(bucket="mybucket", key="mydatalake", format="csv")
```

## AWS Profile

Files are synced using `default` AWS profile, you can configure another one:

```py
import ness

dl = ness.dl(bucket="mybucket", key="mydatalake", profile="myprofile")
```

## Command Line

```
Usage: ness sync [OPTIONS] S3_URI

Options:
  --format TEXT   Data lake source format.
  --profile TEXT  AWS profile.
  --table TEXT    Table name to sync.
  --help          Show this message and exit.
```

```sh
ness sync bucket/key --table mytable
```
