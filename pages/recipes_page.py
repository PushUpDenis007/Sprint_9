from locators.recipes_page_locators import RecipesPageLocators as Recipe
from locators.base_page_locators import BasePageLocators as Base
from pages.base_page import BasePage
import allure
from pathlib import Path

APP_DIR = Path(__file__).parent 
ROOT_DIT = APP_DIR.parent

class RecipesPage(BasePage):

    @allure.step('Нажать на кнопку в шапке Рецепты')
    def click_recipes_button (self):
        self.click_element(Base.recipes_button) 

    @allure.step('Нажать на кнопку в шапке Создать рецепт')
    def click_create_recipe_button (self):
        self.click_element(Base.create_recipe_button) 

    @allure.step('Заполнить Название рецепта')
    def fill_name_input (self,name):
        self.wait_for_located (Recipe.name_input)
        self.send_keys (Recipe.name_input,name)

    @allure.step('Добавить ингредиент')
    def fill_ingredient_name (self,ingredient):
        self.send_keys (Recipe.igredient_name_input,ingredient)
        self.wait_for_clickable(Recipe.INGREDIENT_BY_NAME(ingredient))
        self.click_element(Recipe.INGREDIENT_BY_NAME(ingredient))

    @allure.step('Добавить количество ингредиента')
    def fill_ingredient_amount (self,amount):
        self.send_keys (Recipe.igredient_amount_input,amount)

    @allure.step('Добавить количество ингредиента')
    def click_add_ingredient_button (self):
        self.click_element (Recipe.add_ingredient_button)

    @allure.step('Заполнить Время приготовления')
    def fill_time_input (self,time):
        self.send_keys(Recipe.time_input,time)

    @allure.step('Заполнить Время приготовления')
    def fill_description_area (self,text):
        self.send_keys(Recipe.descripion_area,text)

    @allure.step('Загрузить фото')
    def fill_image (self,file_name):
        image_path = ROOT_DIT / 'assets' / file_name
        absolute_path = str(image_path.resolve())
        self.send_keys(Recipe.add_image_input,absolute_path)

    @allure.step('Нажать на кнопку подтверждения Создания рецепта')
    def click_create_recipe_confirm_button (self):
        self.click_element(Recipe.create_button)    

    @allure.step('Дождаться появления изображения заказа')
    def locate_recipe_image (self):
        return self.wait_for_located(Recipe.image)

    @allure.step('Проверить карточку созданного рецепта')
    def check_card_in_cards_list (self,id):
        return self.wait_for_located(Recipe.CARD_BY_ID(id))

    @allure.step('Получить название рецепта')
    def get_card_name (self,id):
        return self.get_text(Recipe.CARD_BY_ID(id))   