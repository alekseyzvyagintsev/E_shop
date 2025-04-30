##################################################################################################
import pytest

from src.models.category import Category
from src.models.iterator import ProductIterator
from src.models.product import Product


# Фикстуры для инициализации объектов
@pytest.fixture
def iterator(category_with_products):
    return ProductIterator(category_with_products)

@pytest.fixture
def first_product() -> Product:
    return Product(
        "Samsung Galaxy C23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        20000.0,
        5,
    )


@pytest.fixture
def second_product() -> Product:
    return Product(
        "Galaxy Note",
        "",
        8000.00,
        5
    )


@pytest.fixture
def third_product() -> Product:
    return Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        30000.0,
        10
    )


@pytest.fixture
def fake_product():  # type: ignore
    return {'name': 'Rectangle', 'width': 5, 'height': 10}  # type: ignore


@pytest.fixture
def create_category() -> Category:
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство общения",
        products=[],
    )


@pytest.fixture
def category_with_products(create_category, first_product, second_product, third_product) -> Category:
    products = create_category
    products.add_product(first_product)
    products.add_product(second_product)
    products.add_product(third_product)
    return products


@pytest.fixture
def create_product_from_dict() -> Product:
    return Product.new_product(
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )


##################################################################################################
