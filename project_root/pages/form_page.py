# pages/form_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from project_root.pages.base_page import BasePage
import time


class FormPage(BasePage):
    """
    Page Object для страницы с формой practice-automation.com/form-fields/
    """
    
    # URL страницы
    URL = "https://practice-automation.com/form-fields/"
    
    # Локаторы элементов формы
    NAME_FIELD = (By.ID, "name-input")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type='password']")
    FAVORITE_DRINK_CHECKBOXES = (By.NAME, "drink")
    FAVORITE_COLOR_DROPDOWN = (By.ID, "color")
    AUTOMATION_SELECT = (By.ID, "automation")
    EMAIL_FIELD = (By.ID, "email")
    MESSAGE_FIELD = (By.ID, "message")
    SUBMIT_BUTTON = (By.ID, "submit-btn")

    def __init__(self, driver):
        super().__init__(driver)
    
    def open_form_page(self):
        """Открыть страницу с формой"""
        self.open_url(self.URL)
        return self
    
    def fill_name_field(self, name):
        """Заполнить поле Name"""
        self.send_keys_to_element(self.NAME_FIELD, name)
        return self
    
    def fill_password_field(self, password):
        """Заполнить поле Password"""
        self.send_keys_to_element(self.PASSWORD_FIELD, password)
        return self

    def select_favorite_drinks(self, drinks):
        checkboxes = self.driver.find_elements(By.CSS_SELECTOR, "input[name='fav_drink']")
        for checkbox in checkboxes:
            if checkbox.get_attribute("value") in drinks:
                if not checkbox.is_selected():
                    checkbox.click()
        return self

    def select_favorite_color(self, color):
        self.driver.find_element(By.CSS_SELECTOR, f"input[name='fav_color'][value='{color}']").click()
        return self

    def select_automation_preference(self, text):
        select = Select(self.driver.find_element(*self.AUTOMATION_SELECT))
        select.select_by_visible_text(text)
    
    def fill_email_field(self, email):
        """Заполнить поле Email"""
        self.send_keys_to_element(self.EMAIL_FIELD, email)
        return self

    def fill_message_with_tools(self):
        """Получить информацию об элементах  и заполнить форму Message"""
        tools_elements = self.driver.find_elements(By.XPATH,
                                                   "//label[text()='Automation tools']/following-sibling::ul/li")
        tools = [el.text for el in tools_elements]
        message_text = f"Количество инструментов: {len(tools)}. Самый длинный инструмент: {max(tools, key=len)}"
        self.driver.find_element(By.ID, "message").send_keys(message_text)
        time.sleep(2)
        return self
    
    def submit_form(self):
        """Нажать кнопку Submit"""
        self.scroll_to_element(self.SUBMIT_BUTTON)
        self.click_element(self.SUBMIT_BUTTON)
        return self
    
    def get_alert_text_and_accept(self):
        """Получить текст алерта и принять его"""
        return self.wait_for_alert_and_accept()
