from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestDatabaseData:
    EXPECTED_BUNS = [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
    ]

    EXPECTED_INGREDIENTS = [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_FILLING, "sausage", 300),
    ]
    
class TestBurgerReceiptData:
    RECEIPT_TEST_DATA = [
        ([], [
            "(==== test_bun ====)",
            "(==== test_bun ====)",
            "",
            "Price: 2000.0"
        ]),
        (['mock_filling'], [
            "(==== test_bun ====)",
            "= filling test_filling =",
            "(==== test_bun ====)",
            "",
            "Price: 2500.0"
        ]),
        (['mock_sauce'], [
            "(==== test_bun ====)",
            "= sauce test_sauce =",
            "(==== test_bun ====)",
            "",
            "Price: 2050.0"
        ]),
        (['mock_filling', 'mock_sauce'], [
            "(==== test_bun ====)",
            "= filling test_filling =",
            "= sauce test_sauce =",
            "(==== test_bun ====)",
            "",
            "Price: 2550.0"
        ])
    ]
