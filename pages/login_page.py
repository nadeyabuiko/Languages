from .base_page import BasePage
from .locators import LoginPageLocators
import secrets
import string
import faker

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "It's not login URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def register_new_user(self, browser):
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(9))

        f = faker.Faker()
        email = f.email()
        browser.find_element(*LoginPageLocators.EMAIL_ADDRESS_REGISTER).send_keys(email)
        browser.find_element(*LoginPageLocators.PASSWORD_REGISTER).send_keys(password)
        browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_REGISTER).send_keys(password)
        browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

