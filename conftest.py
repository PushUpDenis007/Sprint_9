import pytest, allure
from pages.signup_page import SignupPage
from pages.signin_page import SigninPage
from pages.recipes_page import RecipesPage
from urls import Urls
from webdriver_factory import WebDriverFactory
from helpers import create_user_payload
from locators.signup_page_locators import SignupPageLocators as Signup

def pytest_addoption(parser):
    """Регистрируем параметр командной строки для выбора браузера."""
    parser.addoption(
        "--browser", 
        action="store", 
        default="chrome", 
        help="Браузер для тестов: chrome, firefox"
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
def registration (driver):
    payload = create_user_payload()
    signup_page = SignupPage(driver)
    signup_page.click_signup_button()
    signup_page.wait_for_located (Signup.email_input)
    signup_page.fill_first_name_input(payload ["name"])
    signup_page.fill_last_name_input(payload ["last_name"])
    signup_page.fill_username_input(payload["username"])
    signup_page.fill_email_input(payload["email"])
    signup_page.fill_pass_input(payload["password"])
    signin_page = signup_page.click_signup_confirm_button()
    signin_page.locate_confirm_button()
    return payload

@pytest.fixture
def login(driver,registration):
    signin_page = SigninPage(driver)
    signin_page.fill_email_input(registration["username"])
    signin_page.fill_pass_input(registration ["password"])
    signin_page.click_signin_confirm_button()
    signin_page.locate_signout_button()
    
@pytest.fixture
def signup_page(driver):
    return SignupPage(driver)

@pytest.fixture
def signin_page(driver):
    return SigninPage(driver)

@pytest.fixture
def recipes_page(driver):
    return RecipesPage(driver)