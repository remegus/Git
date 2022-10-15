# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def umn_par(m):
    list, inv = [], []
    a, b = 0, -1
    count = 0
    for i in range(1, m + 1):  # int(input('Введите число :')) + 1):
        list.append(i)
        count += 1
    while 0 < count:
        inv.append(list[a] * list[b])
        a += 1
        b -= 1
        count -= 2
    return inv
    # print(f'Вывод {list} => {inv}')


# print(umn_par(-42))
