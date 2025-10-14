from project_root.pages.form_page import FormPage
import allure


class TestFormFields:

    def test_complete_form_submission(self, browser):

        # Создаем экземпляр страницы
        form_page = FormPage(browser)
        
        # Шаг 1: Открыть страницу с формой
        form_page.open_form_page()
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Step 1 - Open form page",
            attachment_type=allure.attachment_type.PNG
        )

        # Тестовые данные
        test_data = {
            "name": "Test User",
            "password": "TestPassword123",
            "favorite_drinks": ["Milk", "Coffee"],
            "favorite_color": "Yellow",
            "automation_preference": "Yes",  # или "No"
            "email": "testuser@example.com"
        }
        
        # Заполняем форму поэтапно согласно требованиям
        
        # Шаг 2: Заполнить поле Name
        form_page.fill_name_field(test_data["name"])
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Step 2 - Fill Name",
            attachment_type=allure.attachment_type.PNG
        )

        # Шаг 3: Заполнить поле Password
        form_page.fill_password_field(test_data["password"])
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Step 3 - Fill Password",
            attachment_type=allure.attachment_type.PNG
        )

        # Шаг 4: Выбрать Milk и Coffee из списка напитков
        form_page.select_favorite_drinks(test_data["favorite_drinks"])
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Step 4 - Select Drinks",
            attachment_type=allure.attachment_type.PNG
        )

        # Шаг 5: Выбрать Yellow из списка цветов
        form_page.select_favorite_color(test_data["favorite_color"])
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Step 5 - Select Color",
            attachment_type=allure.attachment_type.PNG
        )

        # Шаг 6: Выбрать предпочтение по автоматизации
        form_page.select_automation_preference(test_data["automation_preference"])
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Step 6 - Select Automation Preference",
            attachment_type=allure.attachment_type.PNG
        )

        # Шаг 7: Заполнить Email
        form_page.fill_email_field(test_data["email"])
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Step 7 - Fill Email",
            attachment_type=allure.attachment_type.PNG
        )

        # Шаг 8: Получить информацию об инструментах автоматизации и заполнить Message
        form_page.fill_message_with_tools()
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Step 8 - Fill Message",
            attachment_type=allure.attachment_type.PNG
        )

        # Шаг 9: Нажать кнопку Submit
        form_page.submit_form()

        # Проверка ожидаемого результата: алерт с текстом "Message received!"
        alert_text = form_page.get_alert_text_and_accept()
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Step 10 - After Alert",
            attachment_type=allure.attachment_type.PNG
        )

        # Проверяем, что алерт появился и содержит ожидаемый текст
        assert alert_text is not None, "Алерт не появился после отправки формы"
        assert "Message received!" in alert_text, f"Ожидался текст 'Message received!', но получен: '{alert_text}'"
