class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self) -> str:
        """
        Возвращает строковое представление объекта Item
        """
        return f"{self.name} вес:{self.weight} цена:{self.cost}"

class BackPack:  # рюкзак
    def __init__(self, max_weight):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = max_weight
        self.cost = 0

    def add_item(self, item: Item) -> None:
        """
        Добавляет предмет(item) в этот рюкзак
        """

        free_weight = self.max_weight - self.sum_weight()
        if free_weight >= item.weight:
            self.items.append(item)
        else:
            print(f"Предмет {item.name} слишком тяжелый")

    def show_items(self) -> None:
        """
        Выводит(print'ом) все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """

        for i, item in enumerate(self.items, 1):
            print(f"{i} {item.show()}")

    def sum_weight(self) -> float:
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        return sum([item.weight for item in self.items])

    def sum_cost(self) -> int:
        """
        Возвращает суммарную стоимость всех предметов в рюкзаке
        """
        return sum([item.cost for item in self.items])


# Создаем предметы
item_1 = Item("Гиря", 25, 500)
item_2 = Item("Арбуз", 4, 300)
item_3 = Item("Ноутбук", 2.5, 22500)
item_4 = Item("Кот", 0.5, 250)
item_5 = Item("Кирпич", 10, 100)

# Создаем пустой рюкзак и указываем его вместимость(в кг)
backpack = BackPack(max_weight=40)

# Пытаемся добавлять предметы в рюкзак
backpack.add_item(item_1)
backpack.add_item(item_2)
backpack.add_item(item_3)
backpack.add_item(item_4)
backpack.add_item(item_5)

# Выводим все предметы в рюкзаке
backpack.show_items()

# Выводим стоимость предметов в рюкзаке
print(f'Стоимость предметов в рюкзаке: {backpack.sum_cost()}')
