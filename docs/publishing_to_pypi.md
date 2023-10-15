Publishing to Pypi
==================

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
