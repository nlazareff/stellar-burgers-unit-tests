import pytest
from praktikum.burger import Burger
from data import TestDataReceipt


class TestBurger:
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun
    
    @pytest.mark.parametrize('ingredient', 
                             ['mock_filling', 'mock_sauce'])
    def test_add_ingredient(self, ingredient, request):
        ingredient_fixture = request.getfixturevalue(ingredient)
        
        burger = Burger()
        burger.add_ingredient(ingredient_fixture)

        assert len(burger.ingredients) == 1 and burger.ingredients[0] == ingredient_fixture

    @pytest.mark.parametrize('ingredient', 
                             ['mock_filling', 'mock_sauce'])
    def test_remove_ingredient(self, ingredient, request):
        ingredient_fixture = request.getfixturevalue(ingredient)

        burger = Burger()
        burger.add_ingredient(ingredient_fixture)
        
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 0 and burger.ingredients == []

    def test_move_ingredient(self, mock_filling, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sauce)
        
        burger.move_ingredient(0, 1)
        
        assert burger.ingredients[0] == mock_sauce and burger.ingredients[1] == mock_filling

    @pytest.mark.parametrize('ingredients, expected_price', 
                             [([], 2000.0),
                              (['mock_filling'], 2500.0),
                              (['mock_sauce'], 2050.0),
                              (['mock_filling', 'mock_sauce'], 2550.0),
                              ])
    def test_get_price(self, ingredients, expected_price, mock_bun, request):
        burger = Burger()
        burger.set_buns(mock_bun)
        
        for ingredient_name in ingredients:
            ingredient_fixture = request.getfixturevalue(ingredient_name)
            burger.add_ingredient(ingredient_fixture)
        
        assert burger.get_price() == expected_price

    @pytest.mark.parametrize('ingredients_names, expected_lines', 
                             TestDataReceipt.RECEIPT_TEST_DATA)
    def test_get_receipt(self, ingredients_names, expected_lines, mock_bun, request):
        burger = Burger()
        burger.set_buns(mock_bun)
        
        for ingredient_name in ingredients_names:
            ingredient = request.getfixturevalue(ingredient_name)
            burger.add_ingredient(ingredient)
        
        expected_receipt = "\n".join(expected_lines)

        assert burger.get_receipt() == expected_receipt
