import pytest, allure
from pytest_check import check
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


link = "https://selenium1py.pythonanywhere.com/ru/"
login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
link_product = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
product_name = "Coders at Work"


@pytest.mark.login_guest
@allure.epic("Взаимодействие с корзиной")
@allure.feature("Взаимодействие гостя с корзиной")
class TestGuest:

    @allure.story("Отображение корзины гостю")
    @allure.description("Проверка корректности отображения корзины гостю после добавления продукта")
    def test_displaying_basket_page_to_guest(self, browser):
        with allure.step(f"Откыть страницу {link_product}"):
            product_page = ProductPage(browser, link_product)
            product_page.open()
        with allure.step("Добавить продукт в корзину"):
            product_page.add_product_to_basket()
        with allure.step("Перейти в корзину"):
            product_page.go_to_basket()
            basket_page = BasketPage(browser, browser.current_url)
        with check, allure.step("Проверить что в корзине есть продукты"):
            assert basket_page.check_products_in_basket(), "Продукты в корзине не найдены"
        with check, allure.step(f"Проверить имя товара в корзине - {product_name}"):
            assert basket_page.get_product_name_in_basket() == product_name, f"Неверное имя товара в корзине. ОР: {product_name}, ФР: {basket_page.get_product_name_in_basket()}"
        with check, allure.step("Проверить что кнопка оформления товара кликабельна"):
            assert basket_page.check_checkout_button_is_clickable(),"Кнопка оформления товара должна быть кликабельна"
