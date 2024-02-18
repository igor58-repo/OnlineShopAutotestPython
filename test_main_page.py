import pytest
from smart_assertions import soft_assert, verify_expectations
from .pages.main_page import MainPage


link = "https://selenium1py.pythonanywhere.com/ru/"
login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


@pytest.mark.login_guest
class TestGuest:

    def test_displaying_main_page_to_guest(self, browser):
        main_page = MainPage(browser, link)
        main_page.open()
        assert main_page.check_url() == link, f"Неверная ссылка, ОР: {link}, ФР: {main_page.check_url()}"
        soft_assert(main_page.get_login_link() == f"{link}accounts/login/",
            f"Неверная ссылка на страницу авторизациии. ОР: {login_link}, ФР: {main_page.get_login_link()}")
        soft_assert(main_page.get_dropdown_menu() == 6,
            f"Неверное количество элементов меню. ОР: 6, ФР: {main_page.get_dropdown_menu()}")
        soft_assert(main_page.check_search_form(), "Форма поиска не найдена")
        verify_expectations()
