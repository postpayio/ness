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

### Using Conda:

```sh
conda install -c conda-forge pyarrow ness
```

### Using Pip:

```sh
pip install pyarrow ness
```

## Quickstart

```py
import ness

dl = ness.dl(bucket="mybucket", name="mydatalake")
df = dl.read("mytable")
```

## Sync

```py
# Sync all tables
df = dl.sync()

# Sync a single table
df = dl.sync("mytable")
```

## Format

Specify the input data source format, the default format is `parquet`:

```py
import ness

dl = ness.dl(bucket="mybucket", name="mydatalake", format="csv")
```
