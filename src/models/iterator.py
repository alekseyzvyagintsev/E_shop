#########################################################################################################
from src.models.category import Category
from src.models.product import Product


class ProductIterator:
    """Принимает категорию и при переборе выдает продукт"""

    def __init__(self, category_obj: "Category") -> None:
        self.category = category_obj
        self.index = 0

    def __iter__(self) -> "ProductIterator":
        return self

    def __next__(self) -> "Product":
        if self.index < len(self.category.list_products):
            product_obj = self.category.list_products[self.index]
            self.index += 1
            return product_obj
        else:
            raise StopIteration


if __name__ == "__main__":
    prod1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    prod2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    prod3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    cat = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        [prod1, prod2, prod3],
    )

    iterator = ProductIterator(cat)

    print(next(iterator))
    print(next(iterator))
    for product in iterator:
        print(product)
    for product in iterator:
        print(product)

#########################################################################################################
