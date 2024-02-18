from .base_page import BasePage
from .locators import LoginPageLocators
import selenium.common


class LoginPage(BasePage):

    #регистрация нового пользователя
    def register_new_user(self, email, password):
        try:
            self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
            self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIRST).send_keys(password)
            self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM).send_keys(password)
            self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON_SUBMIT).click()
        except selenium.common.NoSuchElementException:
            assert False, "Elements of registration form not found"