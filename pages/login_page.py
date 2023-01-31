from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators
import time

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
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "no email registration form"
        assert self.is_element_present(*LoginPageLocators.REG_PASS1), "no registration password form"
        assert self.is_element_present(*LoginPageLocators.REG_PASS2), "no registration confirm password form"
        assert True

    def register_new_user(self, email, password):
        self.browser.get("http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASS1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASS2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
        time.sleep(2)