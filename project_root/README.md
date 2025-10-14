# README.md

## 🎯 Цель проекта Selenium PyTest Automation Project
Автоматизировать тестирование формы на странице https://practice-automation.com/form-fields/ согласно техническому заданию:

### Предусловие
1. Открыть браузер Google Chrome 
2. Перейти по ссылке https://practice-automation.com/form-fields/

### Тестовые шаги
1. Заполнить поле Name
2. Заполнить поле Password  
3. Из списка "What is your favorite drink?" выбрать Milk и Coffee
4. Из списка "What is your favorite color?" выбрать Yellow
5. В поле "Do you like automation?" выбрать любой вариант
6. Поле Email заполнить строкой формата name@example.com
7. В поле Message написать количество инструментов из секции "Automation tools" и инструмент с наибольшим количеством символов
8. Нажать на кнопку Submit

### Ожидаемый результат
Появление алерта с текстом "Message received!"

## Установка и настройка

### 1. Клонирование проекта
git clone <repository_url>
cd selenium-pytest-project

### 2. Создание виртуального окружения
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

### 3. Установка зависимостей
pip install -r requirements.txt

### 4. Проверка установки Google Chrome
Убедитесь, что у вас установлен Google Chrome версии 141.0.7390.76 или совместимой.

## Запуск тестов

### Запуск всех тестов
pytest

### Запуск с генерацией результатов в allure-results
pytest --alluredir=allure-results

### Генерация HTML-отчёта из результатов
allure generate allure-results --clean -o allure-report

### Просмотр Allure отчёта в браузере
allure open allure-report
```

Позитивный тест-кейс
ID: TC_POS_001
Название: Успешное заполнение и отправка формы
Приоритет: High
Предусловие: Браузер открыт, пользователь на странице формы
Шаги:
В поле "Name" ввести "Alex G"
В поле "Password" ввести "SecurePass123"
В списке "What is your favorite drink?" выбрать "Wine"
В списке "What is your favorite color?" выбрать "Red"
В поле "Do you like automation?" выбрать "Yes"
В поле "Email" ввести "alex.g@example.com"
В поле "Message" определить количество инструментов и инструмент с наибольшим количеством символов
Нажать кнопку "Submit"
Ожидаемый результат: Появился алерт с текстом "Message received!"

Негативный тест-кейс
ID: TC_NEG_001
Название: Попытка отправки формы с пустым полем Name
Приоритет: Medium
Предусловие: Браузер открыт, пользователь на странице формы
Шаги:
В поле "Name" оставить пустым
В поле "Password" ввести "SecurePass123"
В списке "What is your favorite drink?" выбрать "Wine"
В списке "What is your favorite color?" выбрать "Red"
В поле "Do you like automation?" выбрать "Yes"
В поле "Email" ввести "invalid-email"
В поле "Message" определить количество инструментов и инструмент с наибольшим количеством символов
Нажать кнопку "Submit"
Ожидаемый результат: Алерт НЕ появляется, скролл на незаполненное поле Name
