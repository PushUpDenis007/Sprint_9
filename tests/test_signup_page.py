from locators.signup_page_locators import  SignupPageLocators as Signup
from locators.signin_page_locators import SigninPageLocators as Signin
from urls import Urls
import allure
from helpers import create_user_payload

@allure.feature("Создание аккаунта")
class TestSignupPage:

    @allure.title("Создание аккаунта")
    def test_signup_acc_redirect_signin_page (self,signup_page):
        payload = create_user_payload()
        signup_page.click_signup_button()
        signup_page.wait_for_located (Signup.email_input)
        signup_page.send_keys(Signup.first_name_input, payload ["name"])
        signup_page.send_keys(Signup.last_name_input, payload ["last_name"])
        signup_page.send_keys(Signup.username_input,payload["username"])
        signup_page.send_keys(Signup.email_input,payload["email"])
        signup_page.send_keys(Signup.password_input,payload["password"])
        signup_page.click_signup_confirm_button()
        assert signup_page.wait_for_located(Signin.confirm_button)
        assert signup_page.get_current_url() == Urls.SIGN_IN_URL