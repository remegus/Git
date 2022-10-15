import printy
import func_csv
import func_txt


def add():
    """
    функция добавления контакта
    """
    new_line = []
    new_line.append(printy.text('имя', '1'))
    new_line.append(printy.text('фамилия', '1'))
    new_line.append(printy.text('описание', '1'))
    new_line.append(printy.text('номер телефона', '1'))
    print(new_line)
    vybor = 0
    while vybor != '4':  # отменить изменения = 3, сохранить = 1, сохранить и добавить еще сотрудника = 2
        print('\nКакое действие вы хотите совершить?\n\n1.Сохраанить в csv файле.\n2.Сохранить в txt файле.\n3.Сохранить scv и txt.\n4.Отменить и выйти в главное меню.\n')
        vybor = printy.vybor_func()
        if vybor == '1':
            func_csv.zap_csv(new_line)
            printy.seyf()
            break
        elif vybor == '2':
            func_txt.zap_txt(new_line)
            printy.seyf()
            break
        elif vybor == '3':
            func_csv.zap_csv(new_line)
            func_txt.zap_txt(new_line)
            printy.seyf()
            break
    else:
        print('Изменения отменены')
