from praktikum.bun import Bun


class TestBun:
    def test_bun_constructor_sets_attributes(self):
        bun = Bun('Флюоресцентная булка R2-D3', 99.9)

        assert bun.name == 'Флюоресцентная булка R2-D3'
        assert bun.price == 99.9

    def test_bun_get_name_returns_name(self, bun):
        assert bun.get_name() == bun.name

    def test_bun_get_price_returns_price(self, bun):
        assert bun.get_price() == bun.price
