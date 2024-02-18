import pytest
from smart_assertions import soft_assert, verify_expectations
from .pages.product_page import ProductPage


link_login = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
link_product = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
product_name = "Coders at Work"
product_price = "119,99 £"

@pytest.mark.login_guest
class TestGuest:


    def test_displaying_product_page_to_guest(self, browser):
        product_page = ProductPage(browser, link_product)
        product_page.open()
        soft_assert(product_page.get_product_name() == product_name,
        f"Неверное имя продукта на странице. ОР: {product_name}, ФР: {product_page.get_product_name()}")
        soft_assert(product_page.get_product_price() == product_price,
        f"Неверная цена продукта на странице. ОР: {product_price}, ФР: {product_page.get_product_price()}")
        soft_assert(product_page.check_add_to_basket_button_is_clickable(),
        "Кнопка добавления продукта в корзину не кликабельна")
        soft_assert(product_page.check_add_to_wishlist_button_is_not_clickable(),
        "Кнопка добавления продукта в список желаний должна быть кликабельна")
        verify_expectations()


    def test_guest_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, link_product)
        product_page.open()
        product_page.add_product_to_basket()
        soft_assert(product_page.check_message_after_adding_product_to_basket(),
        "Сообщение о добавлении товара в корзину отсутствует")
        soft_assert(product_page.get_product_name_from_message() == product_name,
        f"Неверное имя продукта в сообщении. ОР: {product_name}, ФР: {product_page.get_product_name_from_message()}")
        soft_assert(product_page.get_basket_cost_from_message() == product_price,
        f"Неверная цена продукта в сообщении. ОР: {product_price}, ФР: {product_page.get_basket_cost_from_message()}")
        verify_expectations()
