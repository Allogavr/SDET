import pytest
import allure
import time
from pages.manager_page import ManagerPage
from utils.helpers import (
    generate_post_code,
    find_customer_closest_to_average_length
)


@allure.epic("Bank Manager")
@allure.feature("Customer Management")
@allure.story("Delete Customer")
@allure.title("Тест удаления клиента с именем, близким к среднему")
@allure.description("""
Тест проверяет функциональность удаления клиента:
1. Создается несколько клиентов
2. Из таблицы получается список имен
3. Вычисляется средняя длина имен
4. Находится клиент с длиной имени, ближайшей к среднему
5. Клиент удаляется
6. Проверяется, что клиент удален из таблицы
""")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_delete_customer_closest_to_average(driver, base_url):
    """Тест: Удаление клиента по средней длине имени"""

    manager_page = ManagerPage(driver)
    manager_page.open_page(base_url)

    # Создаем клиентов с именами разной длины
    test_customers = [
        ("Tom", "Riddle", "1234567891"),
        ("Severus", "Snape", "2345678902"),
        ("Draco", "Malfoy", "3456789013")
    ]

    with allure.step("Создание тестовых клиентов"):
        for first_name, last_name, post_code in test_customers:
            with allure.step(f"Создание клиента: {first_name}"):
                manager_page.click_add_customer_button()
                manager_page.fill_customer_form(first_name, last_name, post_code)
                time.sleep(2)
                manager_page.submit_customer_form()
                manager_page.get_alert_text()

    with allure.step("Открытие таблицы клиентов"):
        manager_page.click_customers_button()
        time.sleep(1)

    with allure.step("Получение списка имен клиентов"):
        all_customer_names = manager_page.get_customer_names()
        allure.attach(str(all_customer_names), name="All Customer Names", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Поиск клиента для удаления"):
        customer_to_delete = find_customer_closest_to_average_length(all_customer_names)
        time.sleep(2)
        allure.attach(customer_to_delete, name="Customer to Delete", attachment_type=allure.attachment_type.TEXT)

    with allure.step(f"Поиск и удаление клиента: {customer_to_delete}"):
        manager_page.search_customer(customer_to_delete)
        manager_page.delete_first_customer()
        time.sleep(2)

    with allure.step("Проверка удаления клиента"):
        # Очищаем поиск для получения всех клиентов
        manager_page.search_customer("")
        time.sleep(3)
        updated_customer_names = manager_page.get_customer_names()
        time.sleep(3)
        allure.attach(str(updated_customer_names), name="Updated Customer Names",
                      attachment_type=allure.attachment_type.TEXT)

        assert customer_to_delete not in updated_customer_names, \
            f"Клиент {customer_to_delete} все еще присутствует в таблице после удаления"


@allure.epic("Bank Manager")
@allure.feature("Customer Management")
@allure.story("Delete Customer")
@allure.title("Тест удаления с динамическими данными")
@allure.description("Тест удаления клиента с использованием динамически генерируемых данных")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_delete_customer_with_generated_data(driver, base_url):
    """Тест: Удаление клиента с динамически сгенерированными данными"""

    manager_page = ManagerPage(driver)
    manager_page.open_page(base_url)

    with allure.step("Создание нескольких клиентов с разной длиной имени"):
        # Создаем клиентов с именами известной длины
        customers = []
        for length in [3, 5, 8]:  # Разные длины имен
            post_code = generate_post_code()
            # Генерируем имя нужной длины (для простоты используем буквы)
            first_name = 'a' * length
            last_name = "Test"

            customers.append(first_name)

            manager_page.click_add_customer_button()
            manager_page.fill_customer_form(first_name, last_name, post_code)
            time.sleep(1)
            manager_page.submit_customer_form()
            manager_page.get_alert_text()

    with allure.step("Выполнение теста удаления"):
        manager_page.click_customers_button()

        all_names = manager_page.get_customer_names()
        customer_to_delete = find_customer_closest_to_average_length(all_names)

        manager_page.search_customer(customer_to_delete)
        manager_page.delete_first_customer()
        time.sleep(1)

        manager_page.search_customer("")
        updated_names = manager_page.get_customer_names()

        assert customer_to_delete not in updated_names, \
            f"Клиент {customer_to_delete} не был удален"
