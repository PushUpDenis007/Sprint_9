import allure
from data import Ingredient

@allure.feature("Создание рецепта")
class TestRecipesPage:

    @allure.title("Создание рецепта")
    def test_valid_signin_redirect_recipes_page (self,recipes_page,login):
        recipes_page.click_create_recipe_button()
        recipes_page.fill_name_input("test_name")
        recipes_page.fill_ingredient_name(Ingredient.WATER)
        recipes_page.fill_ingredient_amount ("5")
        recipes_page.click_add_ingredient_button()
        recipes_page.fill_time_input("5")
        recipes_page.fill_description_area("test_description")
        recipes_page.fill_image("6141174524.jpg")
        recipes_page.click_create_recipe_confirm_button()
        recipes_page.locate_recipe_image()
        id = recipes_page.get_current_url().rstrip('/').split('/')[-1]
        recipes_page.click_recipes_button()
        assert recipes_page.check_card_in_cards_list(id)
        assert recipes_page.get_card_name(id) == "test_name"