from tkinter import Y
import view


x = 0
y = 0


def sum_num():
    x = view.get_value('первое')
    y = view.get_value('второе')
    view.vyvod(x+y)


def vch_num():
    x = view.get_value('первое')
    y = view.get_value('второе')
    view.vyvod(x-y)


def umn_num():
    x = view.get_value('первое')
    y = view.get_value('второе')
    view.vyvod(x*y)


def dln_num():
    x = view.get_value('первое')
    y = view.get_value('второе')
    o = x/y
    if o % 1 == 0:
        o = int(o)
    view.vyvod(o)


def dv_num():
    x = view.get_value('десятичное')
    y = []
    while x > 0.5:
        x = int(x)
        x = x/2
        if x % 1 == 0:
            y.append('0')
        elif x % 1 > 0:
            y.append('1')
    y.reverse()
    y = ''.join(y)
    view.vyvod(y)
