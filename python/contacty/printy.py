import func_csv


def vybor_func():
    v = input('Введите соответствующую цифру :')
    return v


def text(x, q):
    y = input(f'Введите {x} :')
    if q == '2':
        y = y.lower()
    return y


def print_employers():
    print(func_csv.employers)
    func_csv.employers = []


def seyf():
    print('Сохраненно')
