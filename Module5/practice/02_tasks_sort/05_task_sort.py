# 1. Выведите список сотрудников, отсортированный по уменьшению их заработной платы.
# Если у нескольких сотрудников одинаковая ЗП, то добавьте сортировку по Фамилии
# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:

def sort_choice(nums: list, key=lambda x: x, reverse=False) -> None:
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if reverse:
                condition = key(nums[j]) > key(nums[m])
            else:
                condition = key(nums[j]) < key(nums[m])
            if condition:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1


# Дан список сотрудников:
staff = [
    {'name': 'Григорий', 'surname': 'Петров', 'salary': 124300},
    {'name': 'Николай', 'surname': 'Петров', 'salary': 120000},
    {'name': 'Иван', 'surname': 'Павлов', 'salary': 34500},
    {'name': 'Василий', 'surname': 'Кукушкин', 'salary': 162500},
    {'name': 'Василий', 'surname': 'Павлов', 'salary': 34500},
]

sort_choice(staff, key=lambda x: (x['salary'], x['surname'], x['name']), reverse=True)

print("Список сотрудников отсортированный по уменьшению ЗП:")
for item in staff:
    print(f"{item['name']} {item['surname']} {item['salary']}")

sort_choice(staff, key=lambda x: (x['salary'], x['surname'], x['name']))
sum_salary = 0

for elem in staff[:3]:
    sum_salary += elem['salary']

print(f"Сумма трёх самых низких зарплат: {sum_salary}")
