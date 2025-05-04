##################################################################################################
from typing import Any

import pytest

from src.models.category import Category
from src.models.iterator import ProductIterator
from src.models.lawngrass import LawnGrass
from src.models.product import Product
from src.models.smartphone import Smartphone


# Фикстуры для инициализации объектов
@pytest.fixture
def iterator(category_with_products: "Category") -> "ProductIterator":
    return ProductIterator(category_with_products)


@pytest.fixture
def first_product() -> "Product":
    return Product(
        "Samsung Galaxy C23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        20000.0,
        5,
    )


@pytest.fixture
def second_product() -> "Product":
    return Product("Galaxy Note", "", 8000.00, 5)


@pytest.fixture
def third_product() -> "Product":
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 30000.0, 10)


@pytest.fixture
def smartphone():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )


@pytest.fixture
def lawngrass():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
    )

@pytest.fixture
def fake_product() -> dict[str, Any]:
    return {"name": "Rectangle", "width": 5, "height": 10}


@pytest.fixture
def create_category() -> "Category":
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство общения",
        products=[],
    )


@pytest.fixture
def category_with_products(
    create_category: "Category", first_product: "Product", second_product: "Product", third_product: "Product"
) -> Category:
    products = create_category
    products.add_product(first_product)
    products.add_product(second_product)
    products.add_product(third_product)
    return products


@pytest.fixture
def create_product_from_dict() -> "Product":
    return Product.new_product(
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )


##################################################################################################
