from selenium.webdriver.common.by import By


# базовые локаторы
class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_LINK = (By.XPATH, '//div[@class="basket-mini pull-right hidden-xs"]//a[@class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


# локаторы с главной страницы
class MainPageLocators:
    MAIN_LINK = (By.XPATH, '//a[text() = "Oscar"]')
    DROPDOWN_MENU_ITEMS = (By.XPATH, '//ul[@class = "dropdown-menu"]/li/a')
    BASKET_COST = (By.XPATH, '//div[@class="basket-mini pull-right hidden-xs"]/strong/following-sibling::text()')
    SEARCH_FORM = (By.XPATH, '//form[@class = "navbar-form navbar-right"]')


# локаторы со страницы авторизации
class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FIRST = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON_SUBMIT = (By.XPATH, '//button[@name="registration_submit"]')


# локаторы со страницы продукта
class ProductPageLocators:
    ADD_TO_BASKET = (By.XPATH, '//form[@id="add_to_basket_form"]//button[@type="submit"]')
    ADD_TO_WISHLIST = (By.XPATH, '//button[@class="btn btn-lg btn-wishlist"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages')
    PRODUCT_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]//h1')
    PRODUCT_COST = (By.XPATH, '//div[@class="col-sm-6 product_main"]//p[@class="price_color"]')
    PRODUCT_NAME_IN_MESSAGE = (By.XPATH, '(//div[@class="alertinner "]//strong)[1]')
    BASKET_COST_IN_MESSAGE = (By.XPATH, '(//div[@class="alertinner "]//strong)[3]')


# локаторы со страницы корзины
class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_BASKET_IS_EMPTY = (By.XPATH, '//div[@class="content"]//p')
    PRODUCT_NAME_IN_BASKET = (By.XPATH, '//div[@class="col-sm-4"]/h3/a')
    CHECKOUT_BUTTON = (By.XPATH, '//a[@class="btn btn-lg btn-primary btn-block"]')