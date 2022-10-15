# 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение
#  элементов на указанных позициях. Позиции хранятся в списке positions - создайте этот список
# (например: positions = [1, 3, 6]).


def number_4(n):
    position = [1, 3, 6]
    list = []
    y = 0
    count = 0
    pr = 1
    for i in range(-n, n + 1):
        list.append(i)
    for t in position:
        count += 1
    while y < count:
        pr = list[position[y]] * pr
        y += 1
    return pr


# print(number_4(-400))
