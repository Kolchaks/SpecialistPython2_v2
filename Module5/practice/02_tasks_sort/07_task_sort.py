# Призеры олимпиады
# По результатам олимпиады участники награждаются дипломами.
# Набравшие одинаковые баллы получают дипломы одинаковой степени.
# Призером олимпиады считается участник, получивший диплом не хуже III степени.
# По результатам олимпиады определите количество призеров.
# Вход: натуральное число участников(N < 100) и далее N натуральных# чисел – результаты участников.
# Выход: одно число – число призеров.
# Пример:
# Вход
#
# 10 1 3 4 3 5 6 7 7 6 1
# Выход
# 5

def sort_choice(nums: list, key=lambda n: n, reverse=False) -> None:
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


results = [10, 1, 3, 4, 3, 5, 6, 7, 7, 6, 1]

sort_choice(results, reverse=True)
print(results)
# print(list(set(results)))
bronze = list(set(results))[-3]
number_of_winners = sum([1 for i in results if i >= bronze])
print(number_of_winners)
