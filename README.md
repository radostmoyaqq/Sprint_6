# Sprint_6

UI-тесты для учебного сервиса Яндекс Самокат.

## Установка

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Перед запуском тестов необходимо установить браузер Mozilla Firefox.

## Запуск тестов

```bash
pytest --alluredir=allure_results
```

## Генерация отчета Allure

```bash
allure generate allure_results -o allure_report --clean
```
