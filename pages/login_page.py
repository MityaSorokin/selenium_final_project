from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self): # реализуйте проверку на корректный url адрес
        assert self.browser.current_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", "Wrong login URL"
        assert True

    def should_be_login_form(self): # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_NAME), "No login username form"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "No login password form"
        assert True

    def should_be_register_form(self): # реализуйте проверку, что есть форма регистрации на странице
        assert  self.is_element_present(*LoginPageLocators.REG_EMAIL), "no email registration form"
        assert self.is_element_present(*LoginPageLocators.REG_PASS1), "no registration password form"
        assert self.is_element_present(*LoginPageLocators.REG_PASS2), "no registration confirm password form"
        assert True