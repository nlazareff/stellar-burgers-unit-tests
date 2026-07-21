import pytest

from praktikum.burger import Burger
from data import TestBurgerReceiptData


class TestBurger:
    def test_burger_constructor_sets_bun_to_none(self):
        burger = Burger()

        assert burger.bun is None

    def test_burger_constructor_creates_empty_ingredients_list(self):
        burger = Burger()

        assert burger.ingredients == []

    def test_set_buns_sets_bun(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun is mock_bun
    
    @pytest.mark.parametrize('ingredient', 
                             ['mock_filling', 'mock_sauce'])
    def test_add_ingredient_adds_ingredient(self, ingredient, request):
        ingredient_fixture = request.getfixturevalue(ingredient)
        
        burger = Burger()
        burger.add_ingredient(ingredient_fixture)

        assert burger.ingredients[0] is ingredient_fixture

    @pytest.mark.parametrize('ingredient', 
                             ['mock_filling', 'mock_sauce'])
    def test_remove_ingredient_removes_ingredient(self, ingredient, request):
        ingredient_fixture = request.getfixturevalue(ingredient)

        burger = Burger()
        burger.add_ingredient(ingredient_fixture)
        
        burger.remove_ingredient(0)
        
        assert burger.ingredients == []

    def test_move_ingredient_moves_ingredient(self, mock_filling, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sauce)
        
        burger.move_ingredient(0, 1)
        
        assert burger.ingredients == [mock_sauce, mock_filling]

    @pytest.mark.parametrize('ingredient_names, expected_price', 
                             [([], 2000.0),
                              (['mock_filling'], 2500.0),
                              (['mock_sauce'], 2050.0),
                              (['mock_filling', 'mock_sauce'], 2550.0),
                              ])
    def test_get_price_returns_correct_price(self, ingredient_names, expected_price, mock_bun, request):
        burger = Burger()
        burger.set_buns(mock_bun)
        
        for ingredient_name in ingredient_names:
            ingredient_fixture = request.getfixturevalue(ingredient_name)
            burger.add_ingredient(ingredient_fixture)
        
        assert burger.get_price() == expected_price

    @pytest.mark.parametrize('ingredients_names, expected_lines', 
                             TestBurgerReceiptData.RECEIPT_TEST_DATA)
    def test_get_receipt_returns_correct_receipt(self, ingredients_names, expected_lines, mock_bun, request):
        burger = Burger()
        burger.set_buns(mock_bun)
        
        for ingredient_name in ingredients_names:
            ingredient = request.getfixturevalue(ingredient_name)
            burger.add_ingredient(ingredient)
        
        expected_receipt = "\n".join(expected_lines)

        assert burger.get_receipt() == expected_receipt
