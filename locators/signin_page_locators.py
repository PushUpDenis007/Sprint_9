from selenium.webdriver.common.by import By

class SigninPageLocators:
    email_input = (By.XPATH, "//div[./h1[contains(text(), 'Войти на сайт')]]//input[@name='email']")
    password_input = (By.XPATH, "//div[./h1[contains(text(), 'Войти на сайт')]]//input[@name='password']")
    confirm_button = (By.XPATH, "//div[./h1[contains(text(), 'Войти на сайт')]]//button[contains(text(), 'Войти')]")
