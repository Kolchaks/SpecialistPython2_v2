class Point:
    self.x = x
    self.y = y

# Создадим несколько объектов-точек
point1 = Point()
point2 = Point()

# Добавим координаты(свойства) x, y для первой точки
point1.x = 7
point1.y = 8

# Прочитаем значения свойств
print(point1.x)  # 7
print(point1.y)  # 8
# По сути, свойства - это переменные внутри объекта. Объект для свойств является контейнером

# Попытка обратиться к x, y второй точки
# print(point2.x)  <-- ошибка, сейчас свойство x есть только у первой точки
# print(point2.y)  <-- ошибка
