from selenium.webdriver.common.by import By

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
    BASKET_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main>.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main>h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner>strong:nth-child(1)')
    PRICE_MESSAGE = (By.CSS_SELECTOR, '.alertinner>p>strong')