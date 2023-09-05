import pytest
from product import Product


def test_create_normal_product():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    assert bose is not None


def test_exception_without_info():
    with pytest.raises(Exception):
        Product("", price=250, quantity=500)


def test_if_quantity_0_deactivated():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=10)
    assert bose.active is True
    bose.set_quantity(0)
    assert bose.active is False


def test_buying_modifies_quantity():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=100)
    bose.buy(5)
    assert bose._quantity == 95


def test_buying_lager_existing_quantity():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=10)
    with pytest.raises(ValueError):
        bose.buy(251)


pytest.main()
