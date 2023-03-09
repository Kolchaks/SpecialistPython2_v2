class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def __lt__(self, other):
        """
        Сортирует экземпляры класса по выбранному атрибуту
        """
        return self.weight < other.weight

    def show(self) -> str:
        """
        Возвращает строковое представление объекта Item
        """
        return f"{self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:  # рюкзак
    def __init__(self, max_weight):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = max_weight
        self.current_weight = 0
        self.cost = 0

    def add_item(self, item: Item) -> None:
        """
        Добавляет предмет(item) в этот рюкзак
        """

        free_weight = self.max_weight - self.current_weight
        if free_weight >= item.weight:
            self.items.append(item)
            self.current_weight += item.weight
            self.cost += item.cost
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
        summ_weight = sum([item.weight for item in self.items])

        return summ_weight

    def sum_cost(self) -> int:
        """
        Возвращает суммарную стоимость всех предметов в рюкзаке
        """
        summ_cost = sum([item.cost for item in self.items])

        return summ_cost


# Создаем предметы
items = [
    Item("Гиря", 25, 500),
    Item("Арбуз", 4, 300),
    Item("Ноутбук", 2.5, 22500),
    Item("Кот", 0.5, 250),
    Item("Трос", 3, 150),
]

items.sort()

# Создаем пустой рюкзак и указываем его вместимость(в кг)
backpack = BackPack(max_weight=10)

# Пытаемся добавлять максимальное кол-во предметов в рюкзак
#  максимальное количество, с учетом ограничения общего веса в рюкзаке. Т.е. берем самые легкие предметы.
for item in items:
    backpack.add_item(item)

# Выводим все предметы в рюкзаке
backpack.show_items()
backpack.sum_cost()
backpack.cost
