from .base_page import BasePage
from .locators import MainPageLocators, BasePageLocators


class MainPage(BasePage):

    # получение ссылки авторизации
    def get_login_link(self):
        return self.browser.find_element(*BasePageLocators.LOGIN_LINK).get_attribute("href")

    # получение выпадающего меню
    def get_dropdown_menu(self):
        return len(self.browser.find_elements(*MainPageLocators.DROPDOWN_MENU_ITEMS))

    # проверка формы поиска
    def check_search_form(self):
        return self.is_element_present(*MainPageLocators.SEARCH_FORM)
