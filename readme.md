# Virtual Store Project

## Environment

1. [Python 3.7](https://www.python.org/downloads/release/python-370/)
2. [virtualenv](https://virtualenv.pypa.io/en/stable/)
3. [Docker](https://www.docker.com/)
4. [SqlLite3](https://www.sqlite.org/index.html)

## Installing environment dependencies

### creating environment

`virtualenv .venv`

#### Activating environment on Windows

`.venv/Scripts/activate.bat`

### Installing dependencies

`pip install -r requirements.txt`

execute command at the root of the project:

`pip install .`

## Testes

* Com o `pytest`

```bash
pip install .
pytest
```

* Com o `coverage`

```terminal
coverage run -m pytest
```