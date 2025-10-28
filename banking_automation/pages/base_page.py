from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    """Базовый класс для всех Page Object классов"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Поиск элемента {locator}")
    def find_element(self, locator):
        """Найти элемент на странице"""
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Поиск всех элементов {locator}")
    def find_elements(self, locator):
        """Найти все элементы на странице"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Клик по элементу {locator}")
    def click(self, locator):
        """Кликнуть по элементу"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ввод текста '{text}' в поле {locator}")
    def input_text(self, locator, text):
        """Ввести текст в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста элемента {locator}")
    def get_text(self, locator):
        """Получить текст элемента"""
        return self.find_element(locator).text

    @allure.step("Получение alert сообщения")
    def get_alert_text(self):
        """Получить текст из alert"""
        try:
            alert = self.wait.until(EC.alert_is_present())
            text = alert.text
            alert.accept()
            return text
        except TimeoutException:
            return None
