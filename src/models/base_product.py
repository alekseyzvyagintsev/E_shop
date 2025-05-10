from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """абстрактный класс для создаваемых продуктов"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> "BaseProduct":
        """Метод для добавления нового продукта"""
        pass
