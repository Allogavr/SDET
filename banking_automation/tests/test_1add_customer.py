import pytest
import allure
import time
from pages.manager_page import ManagerPage
from utils.helpers import generate_post_code, generate_first_name_from_post_code


@allure.epic("Bank Manager")
@allure.feature("Customer Management")
@allure.story("Add Customer")
@allure.title("Тест создания нового клиента")
@allure.description("""
Тест проверяет функциональность создания нового клиента:
1. Генерируется Post Code из 10 цифр
2. На основе Post Code генерируется First Name по правилу преобразования
3. Заполняется форма и отправляется
4. Проверяется успешное добавление клиента
""")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_add_customer(driver, base_url):
    """Тест: Создание клиента (Add Customer)"""

    with allure.step("Генерация тестовых данных"):
        post_code = generate_post_code()
        first_name = generate_first_name_from_post_code(post_code)
        last_name = "TestLastName"

        allure.attach(f"Post Code: {post_code}", name="Test Data", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"First Name: {first_name}", name="Test Data", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Last Name: {last_name}", name="Test Data", attachment_type=allure.attachment_type.TEXT)

    manager_page = ManagerPage(driver)

    with allure.step("Открытие страницы Bank Manager"):
        manager_page.open_page(base_url)

    with allure.step("Переход к форме добавления клиента"):
        manager_page.click_add_customer_button()
        time.sleep(1)

    with allure.step("Заполнение и отправка формы"):
        manager_page.fill_customer_form(first_name, last_name, post_code)
        time.sleep(1)
        manager_page.submit_customer_form()

    with allure.step("Проверка успешного добавления клиента"):
        alert_text = manager_page.get_alert_text()
        allure.attach(str(alert_text), name="Alert Message", attachment_type=allure.attachment_type.TEXT)

        # Проверяем, что появился alert с подтверждением
        assert alert_text is not None, "Alert не появился"
        assert "Customer added successfully" in alert_text or "customerId" in alert_text.lower(), \
            f"Неожиданное сообщение в alert: {alert_text}"

    with allure.step("Проверка наличия клиента в таблице"):
        manager_page.click_customers_button()
        customer_names = manager_page.get_customer_names()

        assert first_name in customer_names, \
            f"Клиент {first_name} не найден в таблице. Доступные имена: {customer_names}"


@allure.epic("Bank Manager")
@allure.feature("Customer Management")
@allure.story("Add Customer")
@allure.title("Тест создания нескольких клиентов")
@allure.description("Тест проверяет возможность создания нескольких клиентов подряд")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_add_multiple_customers(driver, base_url):
    """Тест: Создание нескольких клиентов"""

    manager_page = ManagerPage(driver)
    manager_page.open_page(base_url)

    customers_data = []

    with allure.step("Создание 3 клиентов"):
        for i in range(3):
            with allure.step(f"Создание клиента #{i + 1}"):
                post_code = generate_post_code()
                first_name = generate_first_name_from_post_code(post_code)
                last_name = f"LastName{i + 1}"

                customers_data.append({
                    'first_name': first_name,
                    'last_name': last_name,
                    'post_code': post_code
                })

                manager_page.click_add_customer_button()
                manager_page.fill_customer_form(first_name, last_name, post_code)
                time.sleep(1)
                manager_page.submit_customer_form()

                alert_text = manager_page.get_alert_text()
                assert alert_text is not None, f"Alert не появился для клиента #{i + 1}"

    with allure.step("Проверка всех созданных клиентов в таблице"):
        manager_page.click_customers_button()
        customer_names = manager_page.get_customer_names()

        for customer in customers_data:
            assert customer['first_name'] in customer_names, \
                f"Клиент {customer['first_name']} не найден в таблице"
