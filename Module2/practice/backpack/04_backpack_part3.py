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
        summ_weight = sum([item.weight for item in self.items])
    
        return summ_weight
    
    def sum_cost(self) -> int:
        """
        Возвращает суммарную стоимость всех предметов в рюкзаке
        """
        summ_cost = sum([item.cost for item in self.items])
        
        return summ_cost

    def add_items(self, items: list[Item]):
        """
        :param items: Список вещей(объектов класса Item)
        """
        free_weight = self.max_weight - self.sum_weight()
        if free_weight >= item.weight:
            self.items.append(item)
        else:
            print(f"Предмет {item.name} слишком тяжелый")

        # TODO: реализуйте метод так, чтобы из переданного списка предметов выбиралось и помещалось в рюкзак,
        #  максимальное количество, с учетом ограничения общего веса в рюкзаке. Т.е. берем самые легкие предметы.


# TODO-1: Создаем 5-8 предметов и добавляем их в рюкзак
# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight=15)

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
    backpack.add_items(items) 
    
# Выводим все предметы в рюкзаке
backpack.show_items()
