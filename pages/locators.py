from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_NAME = (By.NAME, "login-username")
    LOGIN_PASSWORD = (By.NAME, "login-password")
    REG_EMAIL = (By.NAME, "registration-email")
    REG_PASS1 = (By.NAME, "registration-password1")
    REG_PASS2 = (By.NAME, "registration-password2")
    LINK = (By.LINK_TEXT, 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/')

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main>.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main>h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner>strong:nth-child(1)')
    PRICE_MESSAGE = (By.CSS_SELECTOR, '.alertinner>p>strong')
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini>span>a")
    BASKET_WITH_ITEM = (By.CSS_SELECTOR, ".col-sm-6.h3")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner")
    BASKET_EMPTY_MESSAGE = (By.XPATH, '//div[@id="content_inner"]//p[contains(text(),"Your basket is empty.")]')