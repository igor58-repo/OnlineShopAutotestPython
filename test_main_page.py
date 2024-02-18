import pytest, allure
from pytest_check import check
from smart_assertions import soft_assert, verify_expectations
from .pages.main_page import MainPage


link = "https://selenium1py.pythonanywhere.com/ru/"
login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


@pytest.mark.login_guest
@allure.epic("Отображение главной страницы гостю")
@allure.feature("Отображение главной страницы гостю")
@allure.description("Проверка корректности отображения главной страницы гостю")
class TestGuest:

    @allure.story("Взаимодействие гостя с главной страницей")
    @allure.description("Проверка отображения главной страницы гостю")
    def test_displaying_main_page_to_guest(self, browser):
        with allure.step(f"Откыть страницу {link}"):
            main_page = MainPage(browser, link)
            main_page.open()
        with check, allure.step(f"Проверить что открывшаяся ссылка - {link}"):
            assert main_page.check_url() == link, f"Неверная ссылка, ОР: {link}, ФР: {main_page.check_url()}"
        with check, allure.step(f"Проверить что ссылка на страницу авторизациии - {login_link}"):
            assert (main_page.get_login_link() == f"{link}accounts/login/", f"Неверная ссылка на страницу авторизациии. ОР: {login_link}, ФР: {main_page.get_login_link()}")
        with check, allure.step("Проверить что количество элементов меню 6"):
            assert main_page.get_dropdown_menu() == 6, f"Неверное количество элементов меню. ОР: 6, ФР: {main_page.get_dropdown_menu()}"
        with check, allure.step("Проверить наличие формы поиска"):
            assert main_page.check_search_form(), "Форма поиска не найдена"
