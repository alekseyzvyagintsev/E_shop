############################################################################################################
import pytest

from src.models.category import Category
from src.models.lawngrass import LawnGrass
from src.models.product import Product
from src.models.smartphone import Smartphone


# Тесты для класса Category
def test_category_attributes(create_category: Category) -> None:
    """Проверка атрибутов объекта Category."""
    assert create_category.name == "Смартфоны"
    assert create_category.products is None
    assert create_category.product_count == 0


def test_empty_category_str(create_category: "Category") -> None:
    """Проверка метода __str__() с пустой категорией."""
    expected_string = "Смартфоны, количество продуктов: 0 шт."
    assert str(create_category) == expected_string


def test_category_str(create_category: "Category", first_product: "Product") -> None:
    """Проверка метода __str__() с категорией содержащей продукт."""
    expected_string = "Смартфоны, количество продуктов: 5 шт."
    create_category.add_product(first_product)
    assert str(create_category) == expected_string


def test_add_product_counter(create_category: "Category", first_product: "Product", second_product: "Product") -> None:
    """Проверяем счетчик продуктов."""

    # Начальное количество продуктов в категории
    initial_product_count = Category.product_count

    # Добавляем первый продукт
    create_category.add_product(first_product)
    new_product_count = Category.product_count
    expected_new_product_count = initial_product_count + 1
    assert new_product_count == expected_new_product_count

    # Добавляем второй продукт
    create_category.add_product(second_product)
    final_product_count = Category.product_count
    expected_final_product_count = initial_product_count + 2
    assert final_product_count == expected_final_product_count


def test_add_product(create_category: "Category", first_product: "Product", second_product: "Product") -> None:
    """Проверка работоспособность метода добавления продукта в категорию"""

    # Добавляем первый продукт
    create_category.add_product(first_product)
    expected_first_string = f"{first_product.name}, {first_product.price} руб. Остаток: {first_product.quantity} шт.\n"
    assert create_category.products == expected_first_string

    # Проверяем наличие обоих продуктов в списке
    create_category.add_product(second_product)
    expected_second_string = (
        f"{first_product.name}, {first_product.price} руб. Остаток: {first_product.quantity} шт.\n"
        f"{second_product.name}, {second_product.price} руб. Остаток: {second_product.quantity} шт.\n"
    )
    assert create_category.products == expected_second_string


def test_add_fake_product(create_category, fake_product):  # type: ignore
    # Пытаемся добавить подставной продукт
    with pytest.raises(TypeError, match=".*должен быть наследником Product"):
        create_category.add_product(fake_product)  # type: ignore


def test_empty_products(create_category: "Category") -> None:
    # Проверка начального состояния
    assert create_category.products is None


def test_add_any_product(
    create_category: "Category", second_product: "Product", smartphone: Smartphone, lawngrass: LawnGrass
) -> None:
    """Проверка добавления продуктов их разных подклассов"""
    create_category.add_product(second_product)
    create_category.add_product(smartphone)
    create_category.add_product(lawngrass)

    assert second_product.name == "Galaxy Note"
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert lawngrass.name == "Газонная трава"


############################################################################################################
