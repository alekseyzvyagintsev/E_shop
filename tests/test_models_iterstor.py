##################################################################################################
import pytest

from src.models.category import Category
from src.models.iterator import ProductIterator


def test_product_iterator(category_with_products: Category, iterator) -> None:
    """
    Проверяем порядок вывода продуктов через next()
    """
    results = []
    while True:
        try:
            results.append(next(iterator))
        except StopIteration:
            break
    assert results == category_with_products.list_products


def test_stop_iteration(iterator):
    """
    Проверка исключения StopIteration при исчерпании продуктов
    """
    count = 0
    while True:
        try:
            next(iterator)
            count += 1
        except StopIteration:
            break
    assert count == len(iterator.category.list_products)


def test_empty_category(create_category: Category) -> None:
    """
    Проверка поведения пустой категории
    """
    empty_cat = create_category
    it = ProductIterator(empty_cat)
    with pytest.raises(StopIteration):
        next(it)
##################################################################################################
