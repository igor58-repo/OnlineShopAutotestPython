import pytest
import allure
from datetime import datetime
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help="Выберите браузер: chrome или firefox")
    parser.addoption('--language', action='store', default="en", help="Выберите язык страницы: en, ru... etc")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        print("\nЗапуск браузера chrome...")
        options_chrome = Options()
        options_chrome.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options_chrome)

    elif browser_name == "firefox":
        print("\nЗапуск браузера firefox...")
        options_firefox = OptionsFirefox()
        options_firefox.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options_firefox)

    else:
        raise pytest.UsageError("--browser_name дложен быть chrome или firefox")

    yield browser
    with allure.step("Делаем скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name=f'Screenshot_{datetime.today()}', attachment_type=AttachmentType.PNG)
    print(f"\n закрытие браузера {browser_name}...")
    browser.quit()
