from selenium.webdriver.common.by import By
import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage():

    @pytest.mark.skip
    def test_guest_should_see_login_link(browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.skip
    def test_guest_can_go_to_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open() #открываем страницу
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url) # выполняем метод страницы - переходим на страницу логина
        login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser, link)
    page.open()
    page.open_basket()
    page.is_basket_empty()



''' test_guest_cant_see_product_in_basket_opened_from_main_page:

Гость открывает главную страницу 
Переходит в корзину по кнопке в шапке сайта
Ожидаем, что в корзине нет товаров
Ожидаем, что есть текст о том что корзина пуста '''

