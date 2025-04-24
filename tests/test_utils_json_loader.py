#########################################################################################################
import json
import os

from src.models.category import Category
from src.models.product import Product
from src.utils import load_data_from_json

# Определим путь к файлу products.json относительно корня проекта
path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data/products.json")


def test_load_data_from_json() -> None:
    # Загружаем реальные данные из файла
    with open(path_to_file, encoding="utf-8") as file:
        raw_data = json.load(file)

    # Проверяем загрузку данных
    result = load_data_from_json(path_to_file)

    # Проверяем корректность результатов
    assert len(result) > 0
    for category in result:
        assert isinstance(category, Category)
        if category.products is not None:
            for product in category.products or []:
                assert isinstance(product, Product)

    # Дополнительные проверки структуры данных
    first_category = result[0]
    assert first_category.name == raw_data[0]["name"]


#########################################################################################################
