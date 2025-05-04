############################################################################################################
import pytest

from src.models.lawngrass import LawnGrass
from src.models.product import Product
from src.models.smartphone import Smartphone


# Тесты для класса Product
def test_product_attributes(first_product: Product) -> None:
    """Проверка атрибутов объекта Product."""
    assert first_product.name == "Samsung Galaxy C23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 20000.0
    assert first_product.quantity == 5


def test_product_after_new_product_from_dict(create_product_from_dict: Product) -> None:
    """Проверка атрибутов объекта Product созданного из словаря."""
    assert create_product_from_dict.name == "Samsung Galaxy C23 Ultra"
    assert create_product_from_dict.description == "256GB, Серый цвет, 200MP камера"
    assert create_product_from_dict.price == 180000.0
    assert create_product_from_dict.quantity == 5


def test_product_after_new_product() -> None:
    """Попытка обратиться к методу без словаря с данными о продукте."""
    assert TypeError("Данные принимаются в виде словаря")


def test_product_str(first_product: Product) -> None:
    """Проверка метода __str__()."""
    expected_str = "Samsung Galaxy C23 Ultra, 20000.0 руб. Остаток: 5 шт.\n"
    assert str(first_product) == expected_str


def test_total_price_and_sum_product_true(first_product: "Product", second_product: "Product") -> None:
    assert first_product.total_price() == 100000.0
    assert second_product.total_price() == 40000.0
    assert first_product + second_product == 140000.0


def test_total_price_fake_product(fake_product):  # type: ignore
    # Пытаемся посчитать подставной продукт
    with pytest.raises(AttributeError):
        fake_product.total_prise()  # type: ignore


def test_sum_with_fake_product(first_product, fake_product):  # type: ignore
    # Пытаемся сложить продукт с подставным продуктом
    with pytest.raises(TypeError):
        first_product + fake_product  # type: ignore


def test_create_smartphone(smartphone) -> None:
    assert smartphone.name == 'Samsung Galaxy S23 Ultra'
    assert smartphone.description == '256GB, Серый цвет, 200MP камера'
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.model == 'S23 Ultra'
    assert smartphone.memory == 256
    assert smartphone.color == 'Серый'

def test_create_lawngrass(lawngrass) -> None:
    assert lawngrass.name == 'Газонная трава'
    assert lawngrass.description == 'Элитная трава для газона'
    assert lawngrass.price == 500.0
    assert lawngrass.quantity == 20
    assert lawngrass.country == 'Россия'
    assert lawngrass.germination_period == '7 дней'
    assert lawngrass.color == 'Зеленый'

def test_sum_simple_product_smartphone_grass_true(
        first_product: "Product",
        smartphone: "Smartphone",
        lawngrass: "LawnGrass"
    ) -> None:
    with pytest.raises(TypeError):
        first_product + smartphone
    with pytest.raises(TypeError):
        first_product + lawngrass
    with pytest.raises(TypeError):
        smartphone + lawngrass


############################################################################################################
