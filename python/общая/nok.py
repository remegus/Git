# 2 Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.


def rt(x):
    lop = []
    while (x % 2) == 0 or (x % 3) == 0 or (x % 5) == 0 or (x % 7) == 0 or (x % 11) == 0:
        if (x % 2) == 0:
            x /= 2
            lop.append('2')
        elif (x % 3) == 0:
            x /= 3
            lop.append('3')
        elif (x % 5) == 0:
            x /= 5
            lop.append('5')
        elif (x % 7) == 0:
            x /= 7
            lop.append('7')
        elif (x % 11) == 0:
            x /= 11
            lop.append('11')
    else:
        x = int(x)
        lop.append(str(x))
    if lop[-1] == '1':
        lop.pop()
    lop = ','.join(lop)
    return lop


print(rt(1681))
