from selenium.webdriver.common.by import By

class SignupPageLocators:
    first_name_input = (By.XPATH, "//div[./h1[contains(text(), 'Регистрация')]]//input[@name='first_name']")
    last_name_input = (By.XPATH, "//div[./h1[contains(text(), 'Регистрация')]]//input[@name='last_name']")
    username_input = (By.XPATH, "//div[./h1[contains(text(), 'Регистрация')]]//input[@name='username']")
    email_input = (By.XPATH, "//div[./h1[contains(text(), 'Регистрация')]]//input[@name='email']")
    password_input = (By.XPATH, "//div[./h1[contains(text(), 'Регистрация')]]//input[@name='password']")
    confirm_button = (By.XPATH, "//div[./h1[contains(text(), 'Регистрация')]]//button[contains(text(), 'Создать аккаунт')]")