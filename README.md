# wc
Python implementation of the UNIX wc (Word Count) utility

---
## Install tool
```shell
python3 -m venv venv
source venv/bin/activate
python setup.py develop
```

## Verify installation
```shell
which pywc
pywc hello -n ed
```

---
## Development

Setup environment
```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Install pre-commit hooks
```shell
pre-commit install
```