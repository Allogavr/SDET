from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class ManagerPage(BasePage):
    """Page Object для страницы Bank Manager"""

    # Locators
    ADD_CUSTOMER_BTN = (By.XPATH, "//button[contains(text(),'Add Customer')]")
    OPEN_ACCOUNT_BTN = (By.XPATH, "//button[contains(text(),'Open Account')]")
    CUSTOMERS_BTN = (By.XPATH, "//button[contains(text(),'Customers')]")

    # Add Customer form
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='First Name']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='Last Name']")
    POST_CODE_INPUT = (By.XPATH, "//input[@placeholder='Post Code']")
    ADD_CUSTOMER_SUBMIT_BTN = (By.XPATH, "//button[@type='submit' and text()='Add Customer']")

    # Customers table
    SEARCH_CUSTOMER_INPUT = (By.XPATH, "//input[@placeholder='Search Customer']")
    CUSTOMER_NAMES = (By.XPATH, "//table//tbody//tr/td[1]")
    CUSTOMER_ROWS = (By.XPATH, "//table//tbody//tr")
    DELETE_BUTTONS = (By.XPATH, "//button[contains(text(),'Delete')]")
    FIRST_NAME_HEADER = (By.XPATH, "//a[normalize-space()='First Name']")

    @allure.step("Открытие страницы Bank Manager")
    def open_page(self, url):
        """Открыть страницу менеджера"""
        self.driver.get(url)

    @allure.step("Клик по кнопке 'Add Customer'")
    def click_add_customer_button(self):
        """Кликнуть по кнопке Add Customer"""
        self.click(self.ADD_CUSTOMER_BTN)

    @allure.step("Клик по кнопке 'Customers'")
    def click_customers_button(self):
        """Кликнуть по кнопке Customers"""
        self.click(self.CUSTOMERS_BTN)

    @allure.step("Заполнение формы: First Name={first_name}, Last Name={last_name}, Post Code={post_code}")
    def fill_customer_form(self, first_name, last_name, post_code):
        """Заполнить форму добавления клиента"""
        self.input_text(self.FIRST_NAME_INPUT, first_name)
        self.input_text(self.LAST_NAME_INPUT, last_name)
        self.input_text(self.POST_CODE_INPUT, post_code)

    @allure.step("Отправка формы добавления клиента")
    def submit_customer_form(self):
        """Отправить форму добавления клиента"""
        self.click(self.ADD_CUSTOMER_SUBMIT_BTN)

    @allure.step("Получение списка имен клиентов")
    def get_customer_names(self):
        """Получить список имен клиентов из таблицы"""
        elements = self.find_elements(self.CUSTOMER_NAMES)
        return [elem.text for elem in elements]

    @allure.step("Клик по заголовку столбца 'First Name'")
    def click_first_name_header(self):
        self.click(self.FIRST_NAME_HEADER)

    @allure.step("Поиск клиента по имени: {customer_name}")
    def search_customer(self, customer_name):
        """Поиск клиента в таблице"""
        self.input_text(self.SEARCH_CUSTOMER_INPUT, customer_name)

    @allure.step("Удаление первого клиента из таблицы")
    def delete_first_customer(self):
        """Удалить первого клиента из отфильтрованного списка"""
        delete_buttons = self.find_elements(self.DELETE_BUTTONS)
        if delete_buttons:
            delete_buttons[0].click()
