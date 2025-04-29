import json
import os

from src.models.category import Category
from src.models.product import Product


def load_data_from_json(file_path: str) -> list[Category]:
    """
    Загружает данные из JSON-файла и создаёт объекты классов Product и Category.
    """
    with open(file_path, encoding="utf-8") as file:
        data = json.load(file)

    categories = []
    for category_data in data:
        # Создаем объекты продуктов
        products = [
            Product(
                product["name"],
                product["description"],
                product["price"],
                product["quantity"],
            )
            for product in category_data.get("products", [])
        ]

        # Создаем объект категории
        category = Category(category_data["name"], category_data["description"], products)
        categories.append(category)

    return categories


if __name__ == "__main__":
    path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data/products.json")
    loaded_categories = load_data_from_json(path_to_file)

    # Печать информации о категориях и продуктах
    for category in loaded_categories:
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        print(f"Продукты: {category.products}")
        print("-" * 50)
