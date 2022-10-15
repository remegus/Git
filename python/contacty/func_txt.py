def read_txt():
    """
    читаем файл txt
    """
    h = open('contact_book.txt', 'a+')
    b = h.read()
    h.close()
    b = b.replace(';', ' ')
    print(b)


def zap_txt(fi):
    """
    читаем и дописываем файл txt
    """
    h = open('contact_book.txt', 'a+')
    b = h.read()
    h.close()
    fi = ';'.join(map(str, fi))
    b += '\n' + fi
    h = open('contact_book.txt', 'w')
    h.write(b)
    h.close()


# def de_txt():
#     """
#     удаляем сегмент из файла txt
#     """
