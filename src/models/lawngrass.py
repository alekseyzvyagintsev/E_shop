#################################################################################################
from src.models.product import Product


class LawnGrass(Product):
    """Подкласс класса Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):

        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}, "
                f"{self.name}, "
                f"{self.description}', "
                f"{self.price}, "
                f"{self.quantity}, "
                f"{self.country}, "
                f"{self.germination_period}, "
                f"{self.color}"
                )

#################################################################################################
