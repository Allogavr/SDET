# Banking Project UI Autotests

Проект UI-автотестов для приложения Bank Manager с использованием PyTest, Selenium WebDriver и Allure Reports.

## Описание

Автоматизированное тестирование веб-приложения Bank Manager с полным покрытием основного функционала:
- **URL**: https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager
- **Фреймворк**: PyTest + Selenium WebDriver
- **Паттерн**: Page Object Model
- **Отчеты**: Allure Report
- **Параллелизация**: pytest-xdist
- **CI/CD**: GitHub Actions, GitLab CI, Jenkins

##  Быстрый старт

### 1. Установка

# Создать и активировать виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows

# Установить зависимости
pip install -r requirements.txt

### 2. Запуск тестов

# Базовый запуск
pytest -v

# С Allure отчетом
pytest --alluredir=allure-results
allure serve allure-results

# Параллельный запуск
pytest -n auto -v

##  Тест-кейсы

### TC-001: Создание клиента
- Генерация Post Code (10 цифр)
- Преобразование в First Name (0001252667 → abzap)
- Проверка добавления клиента

### TC-002: Сортировка клиентов
- Клик по заголовку First Name
- Проверка алфавитной сортировки

### TC-003: Удаление клиента
- Расчет среднего арифметического длины имен
- Удаление клиента с ближайшей длиной

Детали в [TEST_CASES.md](TEST_CASES.md)

## Команды запуска

```bash
# По маркерам
pytest -m smoke          # Smoke тесты
pytest -m critical       # Критические тесты
pytest -m regression     # Регрессия

# Параллельно
pytest -n auto           # Авто-определение ядер
pytest -n 4              # 4 процесса

# С отчетами
pytest --alluredir=allure-results --html=report.html
```

## CI/CD

### GitHub Actions
```yaml
# Автоматический запуск при push/PR
# Параллельное выполнение
# Публикация Allure отчетов
```
