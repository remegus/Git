# .Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


def nefib(x):  # = int(input('Введите число :'))
    pr = 0  # фибаначи
    ns = 0
    bd = 0
    count = 0
    rez = []
    while 0 < x:
        if ns == 0:
            ns += 1
        else:
            bd = ns + pr
            pr = ns
            ns = bd
            x -= 1
            count += 1
        rez.append(pr)
    top = []
    inv = 0
    while count >= 1:
        if (count % 2) == 0:
            inv = -rez[count]
        else:
            inv = rez[count]
        top.append(inv)
        count -= 1
    otv = top + rez
    return otv
    # print(f' Список "Негафибоначчи" :{otv}')
