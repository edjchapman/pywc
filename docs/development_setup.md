Development Setup
=================

---

## Setup environment
```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Install the pre-commit hooks

```shell
# cd to the root of the repository e.g. /clarion_app
pre-commit install
```

---

## Install in development mode
```shell
python setup.py develop
```

---

## Verify Installation
```shell
which pywc
```

---

## Test
```shell
# With venv activated and packages installed
pytest
```
