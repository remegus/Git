# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11


def summa_chisla(x):
    inv = []
    while x % 1 > 0:
        x *= 10
    while x != 0:
        inv.append(x % 10)
        x //= 10
    y = int(sum(inv))
    return y


# print(summa_chisla('34'))
