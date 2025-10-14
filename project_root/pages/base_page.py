from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time



class BasePage:
    """
    Базовый класс для всех страниц с общими методами
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open_url(self, url):
        """Открыть URL"""
        self.driver.get(url)
        return self
    
    def find_element(self, locator, timeout=10):
        """Найти элемент с ожиданием"""
        return WebDriverWait(self.driver, timeout).until(
            ec.presence_of_element_located(locator)
        )
    
    def find_clickable_element(self, locator, timeout=10):
        """Найти кликабельный элемент с ожиданием"""
        return WebDriverWait(self.driver, timeout).until(
            ec.element_to_be_clickable(locator)
        )
    
    def find_elements(self, locator):
        """Найти несколько элементов"""
        return self.driver.find_elements(*locator)
    
    def click_element(self, locator):
        """Кликнуть по элементу"""
        element = self.find_clickable_element(locator)
        element.click()
        return self
    
    def send_keys_to_element(self, locator, text):
        """Ввести текст в элемент"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return self
    
    def select_dropdown_by_text(self, locator, text):
        """Выбрать опцию в dropdown по тексту"""
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)
        return self
    
    def select_dropdown_by_value(self, locator, value):
        """Выбрать опцию в dropdown по значению"""
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_value(value)
        return self
    
    def get_element_text(self, locator):
        """Получить текст элемента"""
        element = self.find_element(locator)
        return element.text
    
    def get_elements_text(self, locator):
        """Получить текст всех найденных элементов"""
        elements = self.find_elements(locator)
        return [element.text for element in elements]
    
    def is_element_present(self, locator, timeout=5):
        """Проверить присутствие элемента"""
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def wait_for_alert_and_accept(self, timeout=10):
        """Ожидание алерта и его принятие"""
        try:
            alert = WebDriverWait(self.driver, timeout).until(ec.alert_is_present())
            alert_text = alert.text
            alert.accept()
            return alert_text
        except TimeoutException:
            return None
    
    def scroll_to_element(self, locator):
        """Прокрутить к элементу"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)
        return self
