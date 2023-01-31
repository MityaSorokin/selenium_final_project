from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
import math
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented or selector is wrong"

    def open(self):
        self.browser.get(self.url)

    def is_element_present (self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=3):
        try:
            WebDriverWait(self.browser, timeout).until(expected_conditions.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def open_basket(self):
        try:
            self.browser.find_element(*BasePageLocators.BASKET_BUTTON).click()
            return True
        except NoSuchElementException:
            return False

    def is_disappeared(self, how, what, timeout=3):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(expected_conditions.presence_of_element_located((how, what)))
        except TimeoutException:
            return False


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        time.sleep(0.5)
        x = alert.text.split(" ")[2]
        print("this is x -", x)
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        print("this is answer -", answer)
        time.sleep(0.5)
        alert.accept()
        time.sleep(1.5)
        '''
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
            #time.sleep(2)
            #alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        '''
