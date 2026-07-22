# Sprint_6

UI-tests for the Yandex Scooter training service.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Mozilla Firefox must be installed before running the tests.

## Run tests

```bash
pytest --alluredir=allure_results
```

## Generate Allure report

```bash
allure generate allure_results -o allure_report --clean
```
