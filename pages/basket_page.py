from selenium.common import NoSuchElementException

from .base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from .base_page import BasePageLocators
from .product_page import ProductPageLocators

class BasketPage(BasePage):

    def open_basket(self):
        try:
            self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()
            return True
        except NoSuchElementException:
            return False

    def is_basket_empty(self):
        try:
            self.browser.find_element(*ProductPageLocators.BASKET_EMPTY_MESSAGE).click()
            result = True
        except NoSuchElementException:
            result = False

        assert result is True, 'Basket is not empty.'