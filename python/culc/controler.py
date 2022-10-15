import model
import view


def button_clic():
    x = 0
    while x != 6:
        print("""
        Калькулятор:
        Какое действие вы хотите совершить?
        1. Сложение
        2. Вычитание
        3. Умножение
        4. Деление
        5. Перевести число в двоичный вид
        6. Выход
        """)
        x = view.vybor()
        if x == 1:
            model.sum_num()
        elif x == 2:
            model.vch_num()
        elif x == 3:
            model.umn_num()
        elif x == 4:
            model.dln_num()
        elif x == 5:
            model.dv_num()
        else:
            print('До новых встреч!')
