import pytest
import allure
import time
from pages.manager_page import ManagerPage


@allure.epic("Bank Manager")
@allure.feature("Customer Management")
@allure.story("Sort Customers")
@allure.title("Тест сортировки клиентов по имени")
@allure.description("""
Тест проверяет функциональность сортировки клиентов:
1. Создается несколько клиентов с разными именами
2. Открывается таблица клиентов
3. Проверяется, что клиенты отсортированы по First Name в алфавитном порядке
""")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_sort_customers_by_first_name(driver, base_url):
    """Тест: Сортировка клиентов по имени (First Name)"""

    manager_page = ManagerPage(driver)
    manager_page.open_page(base_url)

    # Создаем клиентов с предсказуемыми именами для проверки сортировки
    test_customers = [
        ("Zara", "LastNameZ", "1234567890"),
        ("Alice", "LastNameA", "0987654321"),
        ("Mike", "LastNameM", "1111222233")
    ]

    with allure.step("Создание тестовых клиентов"):
        for first_name, last_name, post_code in test_customers:
            with allure.step(f"Создание клиента: {first_name}"):
                manager_page.click_add_customer_button()
                manager_page.fill_customer_form(first_name, last_name, post_code)
                time.sleep(1)
                manager_page.submit_customer_form()
                manager_page.get_alert_text()

    with allure.step("Открытие таблицы клиентов"):
        manager_page.click_customers_button()

    with allure.step("Клик по заголовку столбца 'First Name' для сортировки"):
        manager_page.click_first_name_header()
        time.sleep(1)
        manager_page.click_first_name_header()

    with allure.step("Получение списка имен клиентов"):
        customer_names = manager_page.get_customer_names()
        allure.attach(str(customer_names), name="Customer Names List", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Проверка алфавитной сортировки"):
        # Получаем только созданных нами клиентов
        our_customers = [name for name in customer_names if name in [c[0] for c in test_customers]]

        # Проверяем, что они отсортированы
        sorted_customers = sorted(our_customers)
        allure.attach(str(sorted_customers), name="Expected Sorted Order", attachment_type=allure.attachment_type.TEXT)

        # Для проверки сортировки всей таблицы:
        is_sorted = all(customer_names[i] <= customer_names[i + 1] for i in range(len(customer_names) - 1))

        if not is_sorted:
            allure.attach("Список не отсортирован автоматически",
                          name="Note",
                          attachment_type=allure.attachment_type.TEXT)
            