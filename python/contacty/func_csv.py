import printy
import csv


employers = []


def search_csv():
    """
    Функция поиска в записной книжке
    """
    count = 0
    rem = printy.text('искомое', 2)
    for item in employers:
        for no in item:
            if isinstance(no, str) and rem in no.lower():
                print(item)
                count += 1
    if count == 0:
        print('Не найдено')


def zap_csv(row):
    """
    функция записи в csv файл
    """
    with open('contact_book.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';')
        spamwriter.writerow(row)


def read_csv():
    """
    функция чтения csv файла
    """
    with open('contact_book.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            employers.append(row)


def de_csv():
    """
    функция удаления сегмента
    """
    rem = printy.text('искомое', '2')
    count = []
    for index, row in enumerate(employers):
        for res in row:
            if isinstance(res, str) and rem in res:
                count.append(index)
                print(row, count)
                break
    for t in reversed(count):
        employers.pop(t)

    with open('contact_book.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';')
        for item in employers:
            spamwriter.writerow(item)
