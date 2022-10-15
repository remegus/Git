# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# start = int(input('Введите количество игрков 1 или 2:'))

import random

print("На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется рандомом")


def player():
    x = int(input('Введите количество игрков 1 или 2:\n'))
    if x == 1 or x == 2:
        return x
    else:
        print('Ввели неверное количество')
        return player()


def vybor():
    v = int(input('Ввдите количество конфет :'))
    if 0 < v and v < 29:
        return v
    else:
        print('Ввели неверное количество')
        return vybor()


x = player()

if x == 1:  # player vs bot
    player_1 = str(input('Введите имя : '))
    player_2 = 'Bot'
    stol = 300
    x = random.randint(1, 2)
    print('Первым ходит игрок №', x)
    while stol > 28:
        if x == 1 and stol > 28:
            print(player_1)
            y = vybor()
            stol -= y
            x = 2
            print(f'На столе осталось {stol} конфет')
        elif x == 2 and stol > 28:
            count = 0
            y = 0
            while y + count + 28 < stol:
                y += 28
                count += 1
            else:
                y = stol - (y + count)
            if y == 0:
                y = random.randint(1, 28)
            print(f'{player_2} Берет {y} конфет')
            stol -= y
            x = 1
            print(f'На столе осталось {stol} конфет')


elif x == 2:  # player vs player
    player_1 = str(input('Введите имя первого игрока : '))
    player_2 = str(input('Введите имя второго игрока : '))
    stol = 100
    x = random.randint(1, 2)
    print('Первым ходит игрок №', x)
    while stol > 28:
        if x == 1 and stol > 28:
            print(player_1)
            y = vybor()
            stol -= y
            x = 2
            print(f'На столе осталось {stol} конфет')
        elif x == 2 and stol > 28:
            print(player_2)
            y = vybor()
            stol -= y
            x = 1
            print(f'На столе осталось {stol} конфет')
if x == 1:
    print(f'Выиграл {player_1}!')
elif x == 2:
    print(f'Выиграл {player_2}!')
