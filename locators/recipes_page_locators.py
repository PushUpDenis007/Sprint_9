from selenium.webdriver.common.by import By

CARD = lambda id: f"//div[contains(@class, 'cardList')]//div[contains(@class, 'card__body')]//a[@href='/recipes/{id}']"
INGREDIENT_IN_LIST = lambda text: f"//div[contains(@class, 'ingredientsInputs')]/div[3]/div[text()= '{text}']"
class RecipesPageLocators:
    CARD_BY_ID = lambda id: (By.XPATH, CARD(id)) #имя через .text
    INGREDIENT_BY_NAME = lambda text: (By.XPATH, INGREDIENT_IN_LIST(text)) #.click()
    name_input = (By.XPATH, "//label[./div[contains(text(), 'Название рецепта')]]/input")
    igredient_name_input = (By.XPATH, "//label[./div[contains(text(), 'Ингредиенты')]]/input")
    igredient_amount_input = (By.XPATH, "//div[contains(@class, 'ingredientsAmountInput')]//input")
    add_ingredient_button = (By.XPATH, "//div[contains(text(), 'Добавить ингредиент')]")
    time_input = (By.XPATH, "//label[./div[contains(text(), 'Время приготовления')]]/input")
    descripion_area = (By.XPATH, "//label[./div[contains(text(), 'Описание рецепта')]]/textarea")
    add_image_input = (By.XPATH, "//input[contains(@class, 'fileInput')]")
    create_button = (By.XPATH, "//button[contains(text(), 'Создать рецепт')]")
    image = (By.XPATH, "//img[contains(@class, 'single-card__image')]")
