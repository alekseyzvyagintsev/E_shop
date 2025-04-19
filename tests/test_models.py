import pytest

from src.models.category import Category
from src.models.product import Product

# Fixtures для инициализации объектов
@pytest.fixture
def create_product():
    return Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0, quantity=5
    )

@pytest.fixture
def create_category(create_product):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство общения",
        products=[create_product]
    )

# Тесты для класса Product
def test_product_attributes(create_product):
    """Проверка атрибутов объекта Product."""
    assert create_product.name == "Samsung Galaxy C23 Ultra"
    assert create_product.description == "256GB, Серый цвет, 200MP камера"
    assert create_product.price == 180000.0
    assert create_product.quantity == 5

def test_product_repr(create_product):
    """Проверка метода __repr__()."""
    expected_representation = "\nSamsung Galaxy C23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.00 руб. Остаток: 5 шт."
    assert repr(create_product) == expected_representation

# Тесты для класса Category
def test_category_attributes(create_category):
    """Проверка атрибутов объекта Category."""
    assert create_category.name == "Смартфоны"
    assert len(create_category.products) == 1
    assert create_category.count_products == 1

def test_category_str(create_category):
    """Проверка метода __str__()."""
    expected_string = 'Категория "Смартфоны" содержит 1 товар(а/ов)'
    assert str(create_category) == expected_string