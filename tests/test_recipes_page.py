from locators.base_page_locators import BasePageLocators as Base
from locators.recipes_page_locators import RecipesPageLocators as Recipes
import allure
from helpers import login
from data import Ingredient

@allure.feature("Создание рецепта")
class TestRecipesPage:

    @allure.title("Создание рецепта")
    def test_valid_signin_redirect_recipes_page (self,recipes_page):
        login(recipes_page)
        recipes_page.click_create_recipe_button()
        recipes_page.wait_for_located(Recipes.name_input)
        recipes_page.fill_name_input("test_name")
        recipes_page.fill_ingredient_name(Ingredient.WATER)
        recipes_page.fill_ingredient_amount ("5")
        recipes_page.click_add_ingredient_button()
        recipes_page.fill_time_input("5")
        recipes_page.fill_description_area("test_description")
        recipes_page.fill_image("6141174524.jpg")
        recipes_page.click_create_recipe_confirm_button()
        recipes_page.wait_for_located(Recipes.image)
        id = recipes_page.get_current_url().rstrip('/').split('/')[-1]
        recipes_page.click_element(Base.recipes_button)
        assert recipes_page.wait_for_located(Recipes.CARD_BY_ID(id))
        assert recipes_page.get_text(Recipes.CARD_BY_ID(id)) == "test_name"

