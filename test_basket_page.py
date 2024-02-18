import pytest
from smart_assertions import soft_assert, verify_expectations
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


link = "https://selenium1py.pythonanywhere.com/ru/"
login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
link_product = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
product_name = "Coders at Work"


@pytest.mark.login_guest
class TestGuest:

    def test_displaying_basket_page_to_guest(self, browser):
        product_page = ProductPage(browser, link_product)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        soft_assert(basket_page.check_products_in_basket(), "Продукты в корзине не найдены")
        soft_assert(basket_page.get_product_name_in_basket() == product_name,
        f"Неверное имя товара в корзине. ОР: {product_name}, ФР: {basket_page.get_product_name_in_basket()}")
        soft_assert(basket_page.check_checkout_button_is_clickable(),
        "Кнопка оформления товара должна быть кликабельна")
        verify_expectations()
