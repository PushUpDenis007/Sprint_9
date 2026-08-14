from selenium.webdriver.common.by import By

class BasePageLocators:
    signup_button = (By.XPATH, "//a[contains(text(), 'Создать аккаунт')]")
    signin_button = (By.XPATH, "//a[contains(text(), 'Войти')]")
    signout_button = (By.XPATH, "//a[contains(text(), 'Выход')]")
    recipes_button = (By.XPATH, "//a[contains(text(), 'Рецепты')]")
    create_recipe_button = (By.XPATH, "//a[contains(text(), 'Создать рецепт')]")
