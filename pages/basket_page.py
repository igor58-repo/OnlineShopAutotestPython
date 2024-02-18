from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    # проверка наличия продуктов в корзине
    def check_products_in_basket(self):
        return self.is_element_present(*BasketPageLocators.BASKET_ITEMS)

    # получение имени продукта в корзине
    def get_product_name_in_basket(self):
        return self.browser.find_element(*BasketPageLocators.PRODUCT_NAME_IN_BASKET).text

    # проверка что кнопка оформления заказа кликабельна
    def check_checkout_button_is_clickable(self):
        return self.is_element_clickable(*BasketPageLocators.CHECKOUT_BUTTON)
