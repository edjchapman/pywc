Publishing to Pypi
==================

---

## Get Pypi API Token
Get API token from test Pypi
https://pypi.org/manage/account/

---

## Release to Pypi
Releasing is handled by the publish.yml GitHub Action.

Requirements for release:
- Bump version in setup.py
- Create GitHub release with a tag that matches the version in setup.py
