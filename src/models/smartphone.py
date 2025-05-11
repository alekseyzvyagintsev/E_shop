####################################################################################################
from src.models.product import Product


class Smartphone(Product):
    """Подкласс класса Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}, "
            f"{self.name}, "
            f"{self.description}', "
            f"{self.price}, "
            f"{self.quantity}, "
            f"{self.efficiency}, "
            f"{self.model}, "
            f"{self.memory}, "
            f"{self.color}"
        )


####################################################################################################
