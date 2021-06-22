from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес/ что подстрока "login" есть в текущем url браузера. Для этого используйте соответствующее свойство Webdriver.
        assert "login" in str(self.browser.current_url), "Should be login page"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "There is no registration form"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_EMAIL)
        pass_input_1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PASSWORD_1)
        pass_input_2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PASSWORD_2)
        email_input.send_keys(email)
        pass_input_1.send_keys(password)
        pass_input_2.send_keys(password)
        login_button = self.browser.find_element_by_css_selector(".register_form .btn-primary")
        login_button.click()

