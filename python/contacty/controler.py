import printy
import func_add
import func_csv
import func_txt


def contact_book():
    vybor = '0'
    while vybor != '6':
        print('\nКонтактная книга.\n\nКакое действие вы хотете совершить?\n1. Найти контакт.\n2.Создать контакт.\n3.Просмотреть файл csv.\n4.Просмотреть файл txt\n5.Удалить из csv.\n6.Выход.\n')
        vybor = printy.vybor_func()
        if vybor == '1':
            func_csv.read_csv()
            func_csv.search_csv()
            func_add.employers = []
        elif vybor == '2':
            func_add.add()
        elif vybor == '3':
            func_csv.read_csv()
            printy.print_employers()
        elif vybor == '4':
            func_txt.read_txt()
        elif vybor == '5':
            func_csv.read_csv()
            func_csv.de_csv()
            printy.print_employers()
    else:
        print('\nДо новых встреч!\n')
