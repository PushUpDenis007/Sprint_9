from urls import Urls
import allure

@allure.feature("Авторизация")
class TestSigninPage:

    @allure.title("Авторизация")
    def test_valid_signin_redirect_recipes_page (self,signin_page, registration):
        signin_page.fill_email_input(registration["username"])
        signin_page.fill_pass_input(registration ["password"])
        signin_page.click_signin_confirm_button()
        assert signin_page.locate_signout_button()
        assert signin_page.get_current_url() == Urls.RECIPES_URL