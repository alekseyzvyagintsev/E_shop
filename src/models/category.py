#############################################################################################################
from typing import Any

from src.models.product import Product


class Category:
    """
    Класс предоставляющий информацию о категории товара,
    количестве товаров в категории и количестве категорий
    """

    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """Инициализация объекта"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        self.__class__.product_count += len(products)
        self.__class__.category_count += 1

    @property
    def products(self) -> str | None:
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str or None

    def __str__(self) -> str:
        return f'Категория "{self.name}" содержит {len(self.__products)} товар(а/ов)'

    def add_product(self, product: Product) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            self.__class__.product_count += 1
        else:
            raise ValueError(f"{product.__name__} должен быть наследником Product!")


if __name__ == "__main__":
    # Создание продуктов
    prod1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    prod2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    prod3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    prod4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 3)

    # Создание категорий
    cat1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        [prod1, prod2, prod3],
    )
    cat2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [prod4],
    )

    # Вывод результатов
    print(cat1)
    print(cat1.products)
    print("-" * 100)

    print(cat2)
    print(cat2.products)
    print("-" * 100)

    # Верные утверждения
    print(f"Количество продуктов равно {Category.product_count}")
    print(f"Количество категорий равно {Category.category_count}")
    print("-" * 100)

    product1 = Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )

    category = Category(
        name="Смартфоны",
        description="Смартфоны, как средство общения",
        products=[product1],
    )

    """Проверка атрибутов объекта Category."""
    print(category.name)
    print(category.products)
    print(category.product_count)

#############################################################################################################
