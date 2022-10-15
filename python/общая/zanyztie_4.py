# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее
# кратное) этих двух чисел.

l = int(input('Введите первое число :'))
k = int(input('Введите второе число :'))


def rt(x):
    lop = []
    count_2 = 0
    count_3 = 0
    while (x % 2) == 0 or (x % 3) == 0:
        if (x % 2) == 0:
            x /= 2
            count_2 += 1
        elif (x % 3) == 0:
            x /= 3
            count_3 += 1
    else:
        lop.append(count_2)
        lop.append(count_3)
        lop.append(int(x))
    return lop


mn = rt(l)
mj = rt(k)
print(mn, mj)
pol = []
q = 0
while 2 != q:
    if mn[q] >= mj[q]:
        pol.append(mn[q])
    elif mn[q] <= mj[q]:
        pol.append(mj[q])
    q += 1
pol.append(mn[q])
pol.append(mj[q])

if pol[2] == pol[3]:
    pol[3] = 1
# print(pol)
q -= 2
d = 0
while 4 != q:
    if q == 0:
        abc = 2 ** pol[q]
    elif q == 1:
        d = 3 ** pol[q]
        abc = abc * d
    else:
        abc = abc * pol[q]
    q += 1
print(f'НОК будет равен :{abc}')
