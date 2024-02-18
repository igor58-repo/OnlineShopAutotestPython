import pytest, allure
from pytest_check import check
from .pages.product_page import ProductPage

link_login = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
link_product = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
product_name = "Coders at Work1"
product_price = "£19.99"


@pytest.mark.login_guest
@allure.epic("Взаимодействие с корзиной")
@allure.feature("Взаимодействие гостя с продуктом")
class TestGuest:

    @allure.story("Отображение страницы продукта гостю")
    @allure.description("Проверка корректности отображения страницы продукта гостю")
    def test_displaying_product_page_to_guest(self, browser):
        with allure.step(f"Откыть страницу {link_product}"):
            product_page = ProductPage(browser, link_product)
            product_page.open()
        with check, allure.step(f"Проверить что имя продукта на странице - {product_name}"):
            assert product_page.get_product_name() == product_name, f"Неверное имя продукта на странице. ОР: {product_name}, ФР: {product_page.get_product_name()}"
        with check, allure.step(f"Проверить что цена продукта на странице - {product_price}"):
            assert product_page.get_product_price() == product_price, f"Неверная цена продукта на странице. ОР: {product_price}, ФР: {product_page.get_product_price()}"
        with check, allure.step("Проверить что кнопка добавления продукта в корзину кликабельна"):
            assert product_page.check_add_to_basket_button_is_clickable(), "Кнопка добавления продукта в корзину не кликабельна"
        with check, allure.step("Проверить что кнопка добавления продукта в список желаний не кликабельна"):
                assert product_page.check_add_to_wishlist_button_is_not_clickable(), "Кнопка добавления продукта в список желаний должна быть кликабельна"

    @allure.story("Добавление продукта в корзину гостем")
    @allure.description("Проверка, что гость может успешно добавить продукт в корзину")
    def test_guest_add_product_to_basket(self, browser):
        with allure.step(f"Откыть страницу {link_product}"):
            product_page = ProductPage(browser, link_product)
            product_page.open()
        with allure.step("Добавить продукт в корзину"):
            product_page.add_product_to_basket()
        with check, allure.step("Проверить, что после добавления продукта в корзину появилось сообщение"):
            assert product_page.check_message_after_adding_product_to_basket(),"Сообщение о добавлении товара в корзину отсутствует"
        with check, allure.step("Проверить, что имя продукта на странице и в сообщении совпадают"):
            assert product_page.get_product_name_from_message() == product_name, f"Неверное имя продукта в сообщении. ОР: {product_name}, ФР: {product_page.get_product_name_from_message()}"
        with check, allure.step("Проверить, что цена продукта на странице и общая стоимость корзины совпадают"):
            assert product_page.get_basket_cost_from_message() == product_price, f"Неверная цена продукта в сообщении. ОР: {product_price}, ФР: {product_page.get_basket_cost_from_message()}"
