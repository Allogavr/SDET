import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser():
    """
    Создает экземпляр браузера Chrome для всех тестов в сессии
    """
    # Настройки Chrome
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # Используем указанную версию Chrome
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.7390.76 Safari/537.36")
    
    # Создаем драйвер
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Устанавливаем неявное ожидание
    driver.implicitly_wait(10)
    
    yield driver
    
    # Закрываем браузер после всех тестов
    driver.quit()


@pytest.fixture(scope="function")
def setup_teardown(browser):
    """
    Выполняет предварительную настройку и очистку для каждого теста
    """
    # Предварительная настройка
    yield browser
    
    # Очистка после теста (можно добавить скриншоты при ошибках)
    pass


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    driver = item.funcargs.get("browser", None)  # или item.instance.driver в зависимости от фикстуры

    if driver:
        # Скриншот при успешном выполнении (после фазы 'call')
        if rep.when == "call" and rep.passed:
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"Screenshot_Passed_{item.name}",
                attachment_type=AttachmentType.PNG
            )
        # Скриншот при падении (как обычно)
        elif rep.when == "call" and rep.failed:
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"Screenshot_Failed_{item.name}",
                attachment_type=AttachmentType.PNG
            )
