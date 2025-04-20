from src.models.product import Product


class Category:
    """
    Класс предоставляющий информацию о категории товара,
    количестве товаров в категории и количестве категорий
    """

    name: str
    description: str
    products: list
    count_category = 0
    count_products = 0

    def __init__(self, name, description, products):
        """Инициализация объекта"""
        self.name = name
        self.description = description
        self.products = products if products else []
        self.__class__.count_products += len(products)
        self.__class__.count_category += 1

    def __str__(self):
        return f'Категория "{self.name}" содержит {len(self.products)} товар(а/ов)'


if __name__ == "__main__":
    # Создание продуктов
    prod1 = Product(
        "Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
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
    print(cat2)
    print(cat2.products)

    # Верные утверждения
    print(f"Количество продуктов равно {Category.count_products}")
    print(f"Количество категорий равно {Category.count_category}")
