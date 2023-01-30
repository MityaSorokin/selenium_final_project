from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import pytest



product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

list_of_failed_num = [7]

urls = [f"{product_base_link}?promo=offer{i}" if i not in list_of_failed_num else
                pytest.param(f"{product_base_link}?promo=offer{i}",
                             marks=pytest.mark.xfail(reason="some bug", strict=True)
                             )
                # list_of_failed_num.append(i)
                for i in range(10)]


@pytest.mark.parametrize('link', urls)
@pytest.mark.skip(reason="no way of currently testing this")
def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.open_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_page()
    print("failed url number -", list_of_failed_num)

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.open_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.open_basket()
    page.should_disappear_success_message()


    '''test_guest_cant_see_success_message_after_adding_product_to_basket: 
    Открываем страницу товара 
    Добавляем товар в корзину 
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present


    test_guest_cant_see_success_message: 
    Открываем страницу товара 
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present


    test_message_disappeared_after_adding_product_to_basket: 
    Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared'''