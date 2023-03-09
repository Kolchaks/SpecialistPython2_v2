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

    def maximum_weight(self):
        return max([[item.weight, item.name] for item in self.items])

    def max_valuable(self):
        return max([[item.cost / item.weight, item.name] for item in self.items])


# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight=10)

# TODO-1: Создаем 5-8 предметов и добавляем их в рюкзак
items = [
    Item("Гиря", 25, 500),
    Item("Арбуз", 4, 300),
    Item("Ноутбук", 2.5, 22500),
    Item("Кот", 0.5, 250),
    Item("Трос", 3, 150),
    Item("Кирпич", 6, 100),
    Item("Сигареты", 0.1, 130),
    Item("Книга", 1.5, 400)
]

items.sort()

# Пытаемся добавлять максимальное кол-во предметов в рюкзак
for item in items:
    backpack.add_item(item)

# Выводим все предметы в рюкзаке
backpack.show_items()

# TODO-2: В рюкзаке найдите самый тяжелый предмет и выведите его на экран
print(f'Самый тяжёлый предмет в рюкзаке {backpack.maximum_weight()[1]} весит: {backpack.maximum_weight()[0]} кг')

# TODO-3: В рюкзаке найдите самый ценный предмет и выведите его на экран
#  ценным предметом, считать предмет, с самым высоким значение цены на единицу веса
#  поиск предмета реализуйте в виде метода .max_valuable()
print(f'Самый ценный предмет в рюкзаке {backpack.max_valuable()[1]}')
