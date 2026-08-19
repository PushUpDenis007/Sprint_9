from urls import Urls
import allure
from helpers import create_user_payload

@allure.feature("Создание аккаунта")
class TestSignupPage:

    @allure.title("Создание аккаунта")
    def test_signup_acc_redirect_signin_page (self,signup_page):
        payload = create_user_payload()
        signup_page.click_signup_button()
        signup_page.fill_first_name_input(payload ["name"])
        signup_page.fill_last_name_input(payload ["last_name"])
        signup_page.fill_username_input(payload["username"])
        signup_page.fill_email_input(payload["email"])
        signup_page.fill_pass_input(payload["password"])
        signin_page = signup_page.click_signup_confirm_button()
        assert signin_page.locate_confirm_button()
        assert signin_page.get_current_url() == Urls.SIGN_IN_URL