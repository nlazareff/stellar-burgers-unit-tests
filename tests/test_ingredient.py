from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestIngredient:
    def test_ingredient_constructor_sets_attributes(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус фирменный Space Sauce', 80.0)

        assert ingredient.type == INGREDIENT_TYPE_SAUCE
        assert ingredient.name == 'Соус фирменный Space Sauce'
        assert ingredient.price == 80.0

    def test_ingredient_get_price_returns_price(self, ingredient):
        assert ingredient.get_price() == ingredient.price
        
    def test_ingredient_get_name_returns_name(self, ingredient):
        assert ingredient.get_name() == ingredient.name

    def test_ingredient_get_type_returns_type(self, ingredient):
        assert ingredient.get_type() == ingredient.type
