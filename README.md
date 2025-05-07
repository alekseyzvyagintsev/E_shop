# Интернет магазин 

## Описание проекта
Проект разрабатывается в рамках обучения и функционал все время растёт.
На данном этапе модули позволяют следующее:
- создавать продукты используя class Product и подклассы Smartphone, и LawnGrass.
- Распределять продукты по категориям используя class Category.
- Подкачивать данные продуктов из json файла и и на основании полученных данных создавать продукты по категориям.

## Структура проекта:
### Корень проекта содержит:
    - README.md - содергит описание проекта.

### Папка src содержит следующие модули:
    - src/models - содержит модули с классами продуктов и категорий:
        - reprmixin - миксин для продукта, выводит в консоль короткую информацию о создаваемом продукте 
        - base_product - абстрактный класс продутов
        - product - наследуется от base_product 
                    содержит одноименный класс для создания продуктов и вывода информации оних.
            """
            Инициализация: - Product(name, description, prise, quantity)
            Информация по продукту: 
                Имя продукта- print(product1.name)
                Описание - print(product1.description)
                Цена - print(product1.price)
                Остаток - print(product1.quantity)
                Остаток в виде отформатированной строки - print(str(product1))
            Изменение цены - new_product.price = 800
            Полная стоимость остатка продукта - print(product1.total_prise)
            Сложение двух однотипных продуктов - print(product1 + product2) 
                                                >>> сложение total_price двух продуктов
            добавления нового продукта из словаря, например при чтении из файла -
                - Product.new_product({
                        "name": "Samsung Galaxy S23 Ultra", 
                        "description": "256GB, Серый цвет, 200MP камера", 
                        "price": 180000.0,
                        "quantity": 5})

            """
        - category - содержит одноименный класс для создания катгорий продуктов и вывода информации оних.
            """
            - Инициализация - Category(name, description, [product1, product2, product3]) 
                                можно без списка существующих продуктов
            - Добавление готовых созданных продуктов в созданнуюкатегорию - smartphone.add_product(product1)
            - Общий остаток продуктов по категории в категории - print(str(smartphone))
            >>> Смартфоны, количество продуктов: 5 шт.
            - Колво продуктов (не остатки) - print(Category.product_count)
            Информация по категории 
                Имя сатегории- print(category1.name)
                Описание - print(category1.description)
                Список продуктов в категории построчн - print(categry.products)
                Список продуктов как есть - print(categori1.list_catgory)
            Объединение двух категорий путем создания новой - combined_category = ctegory1 + category2
            """
        - iterator -  содержит класс ProductIterator получает на вход объект категории с продуктами 
            и выдает по очереди продкуты в строковом исполнеии определенного формата
            """
            Пример использования: - print(next(iterator))
            """
        - lawngrass - содержит подкласс LawnGrass наследник класса Product
            """
            Инициализация:
            LawnGrass(name, description, price, quantity, country, germination_period, color)
            """
        - smartphone - содержит подкласс Smartphone наследник класса Product
            """
            Инициализация:
            Smartphone(name, description, prise, quantity, efficiency, model, memory, color)
            """
    - utils - содержит функцию load_data_from_json для подкачки создания подуктов и категорий продкутов с помощью
            классов Product и Category.
            """
            # Путь к файлу:
            path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data/products.json")
            # Присваиваем данные переменной 
            loaded_categories = load_data_from_json(path_to_file)
            """
### Папка tests содержит тесты на функции и классы проекта:
    - conftest - содержит фикстуры для тестов.
    - test_utils_json_loader - Тест чтения json - файла.
    - test_models_product - Тест правильность работы класса Product 
        по созданию, изменению продктов и выдаче информации о них.
    - test_models_category - Тест правильность работы класса Category
        по созданию, изменению категорий, добавлению продуктов в категорию.
    - test_models_iterstor - тестирует работу класса итератора.
    - test_models_repr_mixin - Тест фактического включения миксина в класс и корректности вывода сообщения

## Установка

1. Клонируйте репозиторий
'''
git clone https://github.com/alekseyzvyagintsev/E_shop.git
'''
2. Установите зависимости
'''
pip install -r requirements.txt
или
poetry install
'''

## Использование
На настоящий момент использовать функционал возможно 
только вызвав функцию какого-либо модуля и передав ей необходимые аргументы.


## Документация
Для подробного ознакомления обратитеcь к [Документации](src/tests/README.md)

## Лицензия
Этот проект лицензирован по [лицензии MIT](LICENSE)
