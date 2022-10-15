print("""
Игра Х и О :
""")

row = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
x = 1
player1 = []
player2 = []


def print_win(y):
    print(f'{row[0]} | {row[1]} | {row[2]}\n{row[3]} | {row[4]} | {row[5]}\n{row[6]} | {row[7]} | {row[8]}')
    print(f'Победил игрок {y}')
    exit()


def field(x, y):
    if x == 1:
        row[0] = y
    elif x == 2:
        row[1] = y
    elif x == 3:
        row[2] = y
    elif x == 4:
        row[3] = y
    elif x == 5:
        row[4] = y
    elif x == 6:
        row[5] = y
    elif x == 7:
        row[6] = y
    elif x == 8:
        row[7] = y
    elif x == 9:
        row[8] = y


def securitu(y):
    ob = set(player1 + player2)
    if ob == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
        print('Кто-то обязательно победит, в следующий раз')
        exit()
    x = int(input(f'Игрок {y} Выберите поле 1-9 :'))
    if x in ob:
        print('место занято')
        securitu(y)
    else:
        seyf(x, y)
        ob = []


def seyf(x, y):
    field(x, y)
    if 'X' == y:
        player1.append(x)
        win(player1, y)
    elif 'O' == y:
        player2.append(x)
        win(player2, y)


def win(w, y):
    w = set(w)
    count = 0
    a1 = [{1, 2, 3}, {1, 4, 7}, {1, 5, 9}, {
        2, 5, 8}, {3, 6, 9}, {3, 5, 7}, {4, 5, 6}, {7, 8, 9}]
    for i in a1:
        for r in i:
            if r in w:
                count += 1
                if count == 3:
                    print_win(y)
        count = 0


while x != 0:
    print(
        f'{row[0]} | {row[1]} | {row[2]}\n{row[3]} | {row[4]} | {row[5]}\n{row[6]} | {row[7]} | {row[8]}')
    if x == 1:
        y = 'X'
        x = securitu(y)
        x = 2
    elif x == 2:
        y = 'O'
        x = securitu(y)
        x = 1
