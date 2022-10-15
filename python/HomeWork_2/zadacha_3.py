# 3.Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: список = [2.0, 2.25, 2.37, 2.44, 2.49, 2.52], сумма = 14.07


def number_3(n):
    list = []
    for i in range(1, n + 1):
        y = (1 + 1/i) ** i
        list.append(round(y, 2))
    return sum(list)


# print(number_3(-12))
# print(list, 'сумма =', sum(list))
