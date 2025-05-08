##########################################################################################################
from typing import Any

from src.models.lawngrass import LawnGrass
from src.models.product import Product
from src.models.smartphone import Smartphone


def test_product_class_withe_repr_mixin(capsys: Any, third_product: "Product") -> None:
    """Тест фактического включения миксина в класс product и корректности вывода сообщения"""
    message = capsys.readouterr()
    assert message.out.strip() == "Product, Xiaomi Redmi Note 11, 1024GB, Синий', 30000.0, 10"


def test_lawngrass_class_withe_repr_mixin(capsys: Any, lawngrass: "LawnGrass") -> None:
    """Тест фактического включения миксина в класс lawngrass и корректности вывода сообщения"""
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass, Газонная трава, Элитная трава для газона', 500.0, 20"


def test_smartphone_class_withe_repr_mixin(capsys: Any, smartphone: "Smartphone") -> None:
    """Тест фактического включения миксина в класс smartphone и корректности вывода сообщения"""
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone, Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера', 180000.0, 5"


##########################################################################################################
