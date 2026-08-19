from locators.signup_page_locators import SignupPageLocators as Signup
from locators.base_page_locators import BasePageLocators as Base
from locators.signin_page_locators import SigninPageLocators as Signin
from pages.base_page import BasePage
from pages.signin_page import SigninPage
import allure

class SignupPage(BasePage):

    @allure.step('Нажать на кнопку в шапке Создать аккаунт')
    def click_signup_button (self):
        self.click_element(Base.signup_button) 

    @allure.step('Заполнить Имя')
    def fill_first_name_input (self,first_name):
        self.send_keys (Signup.first_name_input,first_name)

    @allure.step('Заполнить Фамилию')
    def fill_last_name_input (self,last_name):
        self.send_keys (Signup.last_name_input,last_name)

    @allure.step('Заполнить Имя пользователя')
    def fill_username_input (self,username):
        self.send_keys (Signup.username_input,username)

    @allure.step('Заполнить почту')
    def fill_email_input (self,email):
        self.wait_for_located (Signup.email_input)
        self.send_keys (Signup.email_input,email)

    @allure.step('Заполнить пароль')
    def fill_pass_input (self,password):
        self.send_keys(Signup.password_input,password)

    @allure.step('Дождаться появления кнопки входа')
    def locate_signin_input (self):
        return self.wait_for_located (Signin.confirm_button)

    @allure.step('Нажать на кнопку подтверждения Регистрации')
    def click_signup_confirm_button (self):
        self.click_element(Signup.confirm_button)
        return SigninPage(self.driver) 