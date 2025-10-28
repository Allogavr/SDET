import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации и завершения работы WebDriver"""
    with allure.step("Инициализация браузера Chrome"):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        driver.implicitly_wait(10)

    yield driver

    with allure.step("Закрытие браузера"):
        driver.quit()


@pytest.fixture(scope="session")
def base_url():
    """Базовый URL приложения"""
    return "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"


def pytest_configure(config):
    """
    Настройка маркеров для pytest
    """
    config.addinivalue_line(
        "markers", "smoke: Smoke тесты для быстрой проверки основного функционала"
    )
    config.addinivalue_line(
        "markers", "regression: Регрессионные тесты для полной проверки"
    )
    config.addinivalue_line(
        "markers", "critical: Критически важные тесты"
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук для создания скриншотов при падении тестов
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        if "driver" in item.fixturenames:
            driver = item.funcargs["driver"]
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="Screenshot on failure",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"Failed to take screenshot: {e}")
