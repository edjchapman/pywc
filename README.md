# pywc
Python implementation of the UNIX wc (Word Count) utility

https://test.pypi.org/project/pywc/

---
## Development

Setup environment
```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pre-commit install
```

Install in development mode
```shell
python setup.py develop
```

Verify Installation
```shell
which pywc
pywc hello -n ed
```

---
## Publish
Get API token from test Pypi
https://test.pypi.org/manage/account/token/

```shell
# Build
python setup.py sdist bdist_wheel
# Publish
twine upload --repository testpypi --skip-existing dist/*
```

When prompted:
- Username: `__token__`
- Password: PYPI_API_TOKEN

---
## Install from Pypi
```shell
pip install -i https://test.pypi.org/simple/ pywc
```