import pytest

from src.models.category import Category
from src.models.product import Product


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


# Тесты для класса Category
def test_category_attributes(create_category: Category) -> None:
    """Проверка атрибутов объекта Category."""
    assert create_category.name == "Смартфоны"
    assert create_category.products is None
    assert create_category.product_count == 0


def test_empty_category_str(create_category: 'Category') -> None:
    """Проверка метода __str__() с пустой категорией."""
    expected_string = 'Смартфоны, количество продуктов: 0 шт.'
    assert str(create_category) == expected_string


def test_category_str(create_category: 'Category', first_product: 'Product') -> None:
    """Проверка метода __str__() с категорией содержащей продукт."""
    expected_string = 'Смартфоны, количество продуктов: 5 шт.'
    create_category.add_product(first_product)
    assert str(create_category) == expected_string


def test_add_product_counter(create_category: 'Category', first_product: 'Product', second_product: 'Product') -> None:
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


def test_add_product(create_category: 'Category', first_product: 'Product', second_product: 'Product') -> None:
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
    with pytest.raises(ValueError, match=".*должен быть наследником Product"):
        create_category.add_product(fake_product)  # type: ignore


def test_empty_products(create_category: 'Category') -> None:
    # Сначала проверим начальное состояние
    assert create_category.products is None


def test_class_product_count_increase(create_category: 'Category', first_product: 'Product') -> None:
    # Изначально проверяем количество продуктов в классе
    initial_class_product_count = Category.product_count

    # Добавляем продукт
    create_category.add_product(first_product)

    # Проверяем увеличение количества продуктов в классе
    new_class_product_count = Category.product_count
    expected_new_class_product_count = initial_class_product_count + 1
    assert new_class_product_count == expected_new_class_product_count


def test_total_price_and_sum_product_true(first_product: 'Product', second_product: 'Product') -> None:
    assert first_product.total_price() == 100000.0
    assert second_product.total_price() == 40000.0
    assert first_product + second_product == 140000.0


def test_total_price_fake_product(fake_product):  # type: ignore
    # Пытаемся посчитать подставной продукт
    with pytest.raises(AttributeError):
        fake_product.total_prise()  # type: ignore


def test_sum_with_fake_product(first_product, fake_product):  # type: ignore
    # Пытаемся сложить продукт с подставным продуктом
    with pytest.raises(ValueError):
        first_product + fake_product  # type: ignore
