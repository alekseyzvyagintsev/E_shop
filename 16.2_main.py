from src.models.category import Category
from src.models.lawngrass import LawnGrass
from src.models.product import Product
from src.models.smartphone import Smartphone

if __name__ == '__main__':
    Category.__products = []
    a = Product('a', 'b', 1, 2)
    b = LawnGrass('a', 'b', 1, 2, 'c', 'd', 'e')
    c = Smartphone('aa', 'bb', 11, 3, 98, 'dd', 512, 'ccc')
    # product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    # product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    # product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    #
    # print(product1.name)
    # print(product1.description)
    # print(product1.price)
    # print(product1.quantity)
    # print(f"Первый смарт {'-' * 100}\n")
    #
    # print(product2.name)
    # print(product2.description)
    # print(product2.price)
    # print(product2.quantity)
    # print(f"Второй смарт {'-' * 100}\n")
    #
    # print(product3.name)
    # print(product3.description)
    # print(product3.price)
    # print(product3.quantity)
    # print(f"Третий смарт {'-' * 100}\n")
    #
    # category1 = Category("Смартфоны",
    #                      "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    #                      [product1, product2, product3])
    #
    # print(category1.name == "Смартфоны") # Bool
    # print(category1.description)
    # print(len(category1.products))
    # print(category1.category_count)
    # print(category1.product_count)
    # print(f"Кат Смат {'-' * 100}\n")
    #
    # product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    # category2 = Category("Телевизоры",
    #                      "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    #                      [product4])
    #
    # print(category2.name)
    # print(category2.description)
    # print(len(category2.products))
    # print(category2.products)
    # print(f"Кат Тел {'-' * 100}\n")
    #
    # print(Category.category_count)
    # print(Category.product_count)
    # print(f"Счетчики {'-' * 100}")