[![master-build-status](https://api.travis-ci.org/Guidebook/guidebook-api-python.svg?branch=master)](https://travis-ci.org/Guidebook/guidebook-api-python)

# About

`guidebook-api-python` is a python client for the [Guidebook Open API](https://developer.guidebook.com/).

# Installation

`pip install guidebook-api-python`

# Example Usage

```
from guidebook import api_requestor

api_key = 'example_key'

api_client = api_requestor.APIRequestor(api_key)

api_url = 'http://guidebook.com'

api_client.request('get', api_url)

```


# PyPI Package Management

The `guidebook-api-python` package is owned by the `guidebook-web-team` PyPI user. The `guidebook-web-team` PyPI user is managed by the Guidebook IT team.

Instructions for packaging and uploading to PyPI can be found on the python.org website (generally, you'll be using `python setup.py <command>` and `twine`): https://packaging.python.org/tutorials/distributing-packages/

# Development

## Code Linting

`isort` and `flake8` linting checks are run by Travis CI on the GitHub remote; builds will "fail" if the lint checks discover problems. The `.flake8` and `.isort.cfg` files in the root of this project contain the specific linting configurations that get run by Travis CI. You should be able to just invoke `flake8` and `isort` from the root of this project to run the checks locally -- `flake8` and `isort` will know to look for and use the aforementioned configuration files at the project root.

## Tests

Running tests:

```
python -m unittest discover
```
