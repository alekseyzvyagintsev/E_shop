###########################################################################################################
from typing import Any, Dict, TypeVar

T = TypeVar("T")


class Product:
    """Класс предоставляющий информацию о продукте"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    # def __repr__(self) -> str:
    #     return f"\n{self.name}, {self.description}, {self.price:.2f} руб. Остаток: {self.quantity} шт."

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n"

    def total_price(self) -> float:
        """Суммарная стоимость остатков продукта."""
        if type(self) is Product:
            return self.price * self.quantity
        else:
            raise ValueError(f"{self} должен быть наследником Product!")

    def __add__(self, other) -> Any:
        if type(self) == type(other):
            return self.total_price() + other.total_price()
        else:
            raise ValueError(f"Оба объекта {self} и {other} должны быть наследниками Product!")

    @classmethod
    def new_product(cls: type[T], dict_product: Dict[str, Any]) -> T:
        if isinstance(dict_product, dict):
            return cls(**dict_product)
        else:
            raise TypeError("Данные принимаются в виде словаря")

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price > 0:
            if new_price < self.__price:
                user_choice = input('Вы уверены, что цену нужно снизить? Y/N ')
                if user_choice == 'Y' or user_choice == 'y':
                    self.__price = new_price
                return
        else:
            raise TypeError("Цена не должна быть нулевая или отрицательная")


if __name__ == "__main__":
    prod1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    prod2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    prod3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(prod1)
    print(prod2)
    print(prod3)
    print('-' * 100)

    print(prod1.total_price())
    print(prod2.total_price())
    print(prod3.total_price())
    print('-' * 100)

    print(prod1 + prod2)
    print(prod1 + prod3)
    print('-' * 100)

    # print(prod1.price)
    # prod1.price = 179999.9
    # print(prod1.price)
#     print('-' * 100)

###########################################################################################################
