from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.expected_conditions import NoSuchElementException


class ProductPage(BasePage):

    # добавление товара в корзину
    def add_product_to_basket(self):
        try:
            self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        except NoSuchElementException:
            return False
        return True

    # проверка сообщений после добовления продукта в корзину
    def check_message_after_adding_product_to_basket(self):
        return self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    # получение имени продукта из сообщения
    def get_product_name_from_message(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text

    # получение стоимости корзины из сообщения
    def get_basket_cost_from_message(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_COST_IN_MESSAGE).text

    # получение имени продукта
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    # получение стоимости продукта
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text

    # проверки кликабельности кнопки добавления продукта в корзину
    def check_add_to_basket_button_is_clickable(self):
        return self.is_element_clickable(*ProductPageLocators.ADD_TO_BASKET)

    # проверка что кнопка добавления продукта в список желаний не кликабельна
    def check_add_to_wishlist_button_is_not_clickable(self):
        return self.is_element_not_clickable(*ProductPageLocators.ADD_TO_WISHLIST)
