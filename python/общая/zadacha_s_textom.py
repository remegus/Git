# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


h = open('HomeJack.txt', 'r')
b = h.read()  # читаем файл
h.close()

print(b, '\n')

b = b.replace('\n', ' ')                    # убираем переносы
b = b.split(' ')                            # разбиваем
for ind, lop in enumerate(b):               # находим и удаляем совпадения
    if 'ек' in lop:
        b.pop(ind)

b = ", ".join(b)                            # совмещаем
b = b.replace(',', '')                      # убираем лишнее
b = b.lower()
print(b)

exit()
h = open('text.txt', 'w')
h.write(data)  # записываем результат в файл
h.close()
