import complex
import printy
import redact
import read
import deli


def menu():
    x = 0
    while x != 5:
        print("""
        Добро пожаловать!
            Выберите действие.
            1. Добавить.
            2. Редактировать.
            3. Найти.
            4. Удалить.
            5.Выход
            """)
        x = printy.vybor()
        if x == 1:
            menu_add()
        elif x == 2:
            menu_redact()
        elif x == 3:
            menu_sea()
        elif x == 4:
            menu_del()
    else:
        print('До новых встреч!')


def menu_add():
    x = 0

    while x != 5:
        print("""
    Редактор.
    1. Добавить Учителя.
    2. Добавить студента.
    3. Добавить поток.
    4. Добавить курс
    5.Выход
    """)
        x = printy.vybor()
        if x == 1:
            complex.in_teacher()
        elif x == 2:
            complex.in_student()
        elif x == 3:
            complex.in_stream()
        elif x == 4:
            complex.in_course()


def menu_redact():
    x = 0

    while x != 5:
        print("""
    Добавить.
    1. Редактировать Учителя.
    2. Редактировать студента.
    3. Редактировать поток.
    4. Редактировать курс
    5.Выход
    """)
        x = printy.vybor()
        if x == 1:

            redact.red_teacher()
        elif x == 2:

            redact.red_student()
        elif x == 3:

            redact.red_stream()
        elif x == 4:
            redact.red_course()


def menu_sea():
    x = 0

    while x != 5:
        print("""
    Поиск.
    1. Найти Учителя.
    2. Найти студента.
    3. Найти поток.
    4. Найти курс
    5.Выход
    """)
        x = printy.vybor()
        if x == 1:
            read.tc()
        elif x == 2:
            read.all()
        elif x == 3:
            read.stc()
        elif x == 4:
            read.ci()


def menu_del():
    x = 0

    while x != 5:
        print("""
    Удалить.
    1. Удалить учителя.
    2. Удалить студента.
    3. Удалить поток.
    4. Удалить курс
    5.Выход
    """)
        x = printy.vybor()
        if x == 1:
            read.tc()
            deli.del_teacher()
        elif x == 2:
            read.ss()
            deli.del_student()
        elif x == 3:
            read.stc()
            deli.del_stream()
        elif x == 4:
            read.ci()
            deli.del_course()
