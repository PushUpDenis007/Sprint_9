from locators.signin_page_locators import SigninPageLocators as Signin
from locators.base_page_locators import BasePageLocators as Base
from pages.base_page import BasePage
import allure

class SigninPage(BasePage):

    @allure.step('Нажать на кнопку в шапке Войти')
    def click_signin_button (self):
        self.click_element(Base.signin_button) 

    @allure.step('Заполнить почту')
    def fill_email_input (self,email):
        self.send_keys (Signin.email_input,email)

    @allure.step('Заполнить пароль')
    def fill_pass_input (self,password):
        self.send_keys(Signin.password_input,password)

    @allure.step('Дождаться появления кнопки Вход')
    def locate_confirm_button(self):
        return self.wait_for_located(Signin.confirm_button)
    
    @allure.step('Нажать на кнопку подтверждения Входа')
    def click_signin_confirm_button (self):
        self.click_element(Signin.confirm_button)    

    @allure.step('Дождаться появления кнопки Выход')
    def locate_signout_button (self):
        return self.wait_for_located (Base.signout_button)

    