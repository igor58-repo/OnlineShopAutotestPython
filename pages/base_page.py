from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # открытие страницы в браузере
    def open(self):
        self.browser.get(self.url)

    def check_url(self):
        return self.browser.current_url

    # проверка, что элемент существует
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # проверка, что элемент не существует
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # проверка, что элемент кликабелен
    def is_element_clickable(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return True

    # проверка, что элемент не кликабелен
    def is_element_not_clickable(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return True
        return False

    # проверка, что элемент пропал
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # клик по ссылке авторизации на шапке сайта
    def go_to_login_page(self):
        try:
            self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        except NoSuchElementException:
            return False

    # клик по ссылке на корзину на шапке сайта
    def go_to_basket(self):
        try:
            self.browser.find_element(*BasePageLocators.VIEW_BASKET_LINK).click()
        except NoSuchElementException:
            return False

    # поиск ссылки на страницу авторизации
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    # проверка, что юзер авторизован (через поиск иконки юзера)
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
