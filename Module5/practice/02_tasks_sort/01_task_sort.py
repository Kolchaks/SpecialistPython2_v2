# Сумма с условием
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа a

numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
# Задайте самостоятельно, выбрав произвольное число
a = 13
print(sum([i for i in numbers if i > a]))
