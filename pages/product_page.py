from .base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from .main_page import MainPage
from .locators import ProductPageLocators
from .locators import BasePageLocators
# from .locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
import time

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_basket_button()
        #self.open_basket()
        #self.should_be_product_name()
        self.should_be_product_price()
        self.check_item_name()
        self.check_item_price()


    def should_be_basket_button(self):
        assert self.browser.is_element_present(*BasePageLocators.BASKET_BUTTON), "No basket button found"
        assert True

    def open_basket(self):
        try:
            self.browser.find_element(*BasePageLocators.BASKET_BUTTON).click()
            return True
        except NoSuchElementException:
            return False

    def should_be_product_name(self):
        try:
            print(str(self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text))
            return str(self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text)
        except NoSuchElementException:
            return False

    def should_be_product_price(self):
        try:
            print("price from item page - ", str(self.browser.find_element(*ProductPageLocators.PRICE).text))
            return str(self.browser.find_element(*ProductPageLocators.PRICE).text)
        except NoSuchElementException:
                return None

    def check_item_name(self):
        result = str(self.get_success_message_after_add_product_to_basket())
        product = str(self.should_be_product_name())
        assert result == product, 'Product does not match with expected'

    def get_success_message_after_add_product_to_basket(self):
        WebDriverWait(self.browser, 20).until(
            expected_conditions.presence_of_element_located(ProductPageLocators.SUCCESS_MESSAGE))
        try:
            return str(self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text)
        except NoSuchElementException:
            return None

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"


    def get_price(self):
        try:
            return str(self.browser.find_element(*ProductPageLocators.PRICE).text)
        except NoSuchElementException:
            return None

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"

    def get_price_from_message(self):
        WebDriverWait(self.browser, 20).until(
            expected_conditions.presence_of_element_located(ProductPageLocators.PRICE_MESSAGE))
        try:
            print("price for checking -", str(self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text))
            return str(self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text)
        except NoSuchElementException:
            return None

    def check_item_price(self):
        price = self.get_price()
        price_message = self.get_price_from_message()
        assert price == price_message, 'Price does not match with expected'



