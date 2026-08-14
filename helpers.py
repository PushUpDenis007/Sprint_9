import random
import string
from locators.base_page_locators import BasePageLocators as Base
from locators.signup_page_locators import SignupPageLocators as Signup
from locators.signin_page_locators import SigninPageLocators as Signin

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def create_user_payload():
    name = generate_random_string(10)
    last_name = generate_random_string(10)
    email = f"{generate_random_string(10)}@yandex.ru"
    password = generate_random_string(10)
    username = generate_random_string(10)

    payload = {
        "name": name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "username": username
    }
    return payload

def registration (driver):
        payload = create_user_payload()
        driver.click_element(Base.signup_button)
        driver.wait_for_located (Signup.email_input)
        driver.send_keys(Signup.first_name_input, payload ["name"])
        driver.send_keys(Signup.last_name_input, payload ["last_name"])
        driver.send_keys(Signup.username_input,payload["username"])
        driver.send_keys(Signup.email_input,payload["email"])
        driver.send_keys(Signup.password_input,payload["password"])
        driver.click_element (Signup.confirm_button)
        driver.wait_for_located(Signin.confirm_button)
        return payload

def login(driver):
    payload = registration(driver)
    driver.send_keys(Signin.email_input,payload["username"])
    driver.send_keys(Signin.password_input, payload ["password"])
    driver.click_element(Signin.confirm_button)
    driver.wait_for_located(Base.signout_button)