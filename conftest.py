import pytest, allure
from pages.signup_page import SignupPage
from pages.signin_page import SigninPage
from pages.recipes_page import RecipesPage
from urls import Urls
from webdriver_factory import WebDriverFactory

def pytest_addoption(parser):
    """Регистрируем параметр командной строки для выбора браузера."""
    parser.addoption(
        "--browser", 
        action="store", 
        default="chrome", 
        help="Браузер для тестов: chrome, firefox, edge"
    )

@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    allure.dynamic.parameter("Браузер", browser_name.upper())
    with allure.step(f'Открываем сайт в браузере {browser_name.upper()}'):
        driver = WebDriverFactory.get_driver(browser_name)
        driver.get(Urls.SIGN_IN_URL)
    yield driver
    with allure.step('Закрываем сайт'):
        driver.quit()

@pytest.fixture
def signup_page(driver):
    return SignupPage(driver)

@pytest.fixture
def signin_page(driver):
    return SigninPage(driver)

@pytest.fixture
def recipes_page(driver):
    return RecipesPage(driver)