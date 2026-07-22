# Sprint_6

UI-tests for the Yandex Scooter training service.

UI-тесты для учебного сервиса Яндекс Самокат.

## Установка

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Mozilla Firefox must be installed before running the tests.

## Запуск тестов

```bash
pytest --alluredir=allure_results
```

## Генерация отчета Allure
```bash
allure generate allure_results -o allure_report --clean
```
