from locators.signin_page_locators import SigninPageLocators as Signin
from locators.base_page_locators import BasePageLocators as Base
from urls import Urls
import allure
from helpers import registration

@allure.feature("Авторизация")
class TestSigninPage:

    @allure.title("Авторизация")
    def test_valid_signin_redirect_recipes_page (self,signin_page):
        payload = registration(signin_page)
        signin_page.send_keys(Signin.email_input,payload["username"])
        signin_page.send_keys(Signin.password_input, payload ["password"])
        signin_page.click_signin_confirm_button()
        assert signin_page.wait_for_located(Base.signout_button)
        assert signin_page.get_current_url() == Urls.RECIPES_URL