from data import TestDatabaseData


class TestDatabase:
    def test_database_constructor_creates_buns_and_ingredients(self, database):
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6

    def test_database_constructor_creates_expected_buns_and_ingredients(self, database):
        actual_buns = [(bun.name, bun.price) for bun in database.buns]
        actual_ingredients = [
            (ingredient.type, ingredient.name, ingredient.price)
            for ingredient in database.ingredients
        ]

        assert actual_buns == TestDatabaseData.EXPECTED_BUNS
        assert actual_ingredients == TestDatabaseData.EXPECTED_INGREDIENTS

    def test_available_buns_returns_buns_list(self, database):
        assert database.available_buns() == database.buns

    def test_available_ingredients_returns_ingredients_list(self, database):
        assert database.available_ingredients() == database.ingredients
