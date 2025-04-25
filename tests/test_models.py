import pytest

from src.models.category import Category
from src.models.product import Product


# Фикстуры для инициализации объектов
@pytest.fixture
def first_product() -> Product:
    return Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def second_product() -> Product:
    return Product(name="Galaxy Note", description="", price=799.99, quantity=5)


@pytest.fixture
def fake_product() -> Product:
    return Product(name="Rectangle", width=5, height=10)


@pytest.fixture
def create_category() -> Category:
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство общения",
        products=[],
    )


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


# Тесты для класса Product
def test_product_attributes(first_product: Product) -> None:
    """Проверка атрибутов объекта Product."""
    assert first_product.name == "Samsung Galaxy C23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
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


def test_product_repr(first_product: Product) -> None:
    """Проверка метода __repr__()."""
    expected_representation = (
        "\nSamsung Galaxy C23 Ultra, 256GB, " "Серый цвет, 200MP камера, 180000.00 руб. Остаток: 5 шт."
    )
    assert repr(first_product) == expected_representation


# Тесты для класса Category
def test_category_attributes(create_category: Category) -> None:
    """Проверка атрибутов объекта Category."""
    assert create_category.name == "Смартфоны"
    assert create_category.products is None
    assert create_category.product_count == 0


def test_category_str(create_category: Category) -> None:
    """Проверка метода __str__()."""
    expected_string = 'Категория "Смартфоны" содержит 0 товар(а/ов)'
    assert str(create_category) == expected_string


def test_add_product_counter(create_category: Category, first_product: Product, second_product: Product) -> None:
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


def test_add_product(create_category: Category, first_product: Product, second_product: Product) -> None:
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

    # Пытаемся добавить подставной продукт
    with pytest.raises(ValueError, match=".*должен быть наследником Product"):
        create_category.add_product(fake_product)


def test_empty_products(create_category: Category) -> None:
    # Сначала проверим начальное состояние
    assert create_category.products is None


def test_class_product_count_increase(create_category: Category, first_product: Product) -> None:
    # Изначально проверяем количество продуктов в классе
    initial_class_product_count = Category.product_count

    # Добавляем продукт
    create_category.add_product(first_product)

    # Проверяем увеличение количества продуктов в классе
    new_class_product_count = Category.product_count
    expected_new_class_product_count = initial_class_product_count + 1
    assert new_class_product_count == expected_new_class_product_count
