import pytest
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.fixture(scope='function')
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = 'test_bun'
    bun.get_price.return_value = 1000.0
    
    return bun

@pytest.fixture(scope='function')
def mock_filling():
    filling = Mock()
    filling.get_name.return_value = 'test_filling'
    filling.get_price.return_value = 500.0
    filling.get_type.return_value = INGREDIENT_TYPE_FILLING

    return filling

@pytest.fixture(scope='function')
def mock_sauce():
    sauce = Mock()
    sauce.get_name.return_value = 'test_sauce'
    sauce.get_price.return_value = 50.0
    sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE

    return sauce
