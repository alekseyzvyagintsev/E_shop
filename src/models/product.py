# from src.models.category import Category


class Product:
    """Класс предоставляющий информацию о продукте"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"\n{self.name}, {self.description}, {self.price:.2f} руб. Остаток: {self.quantity} шт."


if __name__ == "__main__":
    prod1 = Product(
        "Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    prod2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    prod3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(prod1)
    print(prod2)
    print(prod3)
