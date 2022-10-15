import printy
import add_inf
import read
import complex
import deli
import sqlite3


def red_teacher():
    read.tc()
    deli.del_teacher()
    complex.in_teacher()
    # con = sqlite3.connect('school_base.db')
    # with con:
    #     cur = con.cursor()
    #     y = printy.id()
    #     cur.execute(f"""select course_id, first_name, last_name, mail, number_phone
    #     from teachers where id = {y};""")
    #     step = cur.fetchone()
    #     con.commit()
    #     vyvod = [*step]
    #     x = 0
    #     while 6 != x:
    #         print(vyvod)
    #         print("""Что вы хотите изменить?
    #     1. Имя
    #     2. Фамилию
    #     3. Почту
    #     4. Номер телефона
    #     5. Курс
    #     6. Выход
    #     """)
    #         x = printy.vybor()
    #         if x == 1:
    #             vyvod[1] = printy.text('новое имя')
    #             cur.execute(
    #                 f"""update teachers set 'first_name' = :slovo where id = {y}""", {'slovo': vyvod[1]})
    #         elif x == 2:
    #             vyvod[2] = printy.text('новую фамилию')
    #             cur.execute(
    #                 f"""update teachers set  'last_name' = :slovo where id = {y}""", {'slovo': vyvod[2]})
    #         elif x == 3:
    #             vyvod[3] = printy.text('новую почту')
    #             cur.execute(
    #                 f"""update teachers set 'mail' = :slovo where id = {y}""", {'slovo': vyvod[3]})
    #         elif x == 4:
    #             vyvod[4] = printy.text('новый номер')
    #             cur.execute(
    #                 f"""update teachers set 'number_phone' = :slovowhere id = {y}""", {'slovo': vyvod[4]})
    #         elif x == 5:
    #             read.ci()
    #             vyvod[0] = printy.integ('другой курс')
    #             cur.execute(
    #                 f"""update teachers set 'course_id' = :slovo where id = {y}""", {'slovo': vyvod[0]})
    #     vyvod = tuple(vyvod)
    #     print(vyvod)
    #     add_inf.add_teacher(vyvod)


def red_student():
    read.ss()
    y = printy.id()
    con = sqlite3.connect('school_base.db')
    with con:
        cur = con.cursor()
        cur.execute(f"""select stream_id, s_first_name, s_last_name, s_mail, s_number_phone 
        from students where id = {y}""")
        step = cur.fetchone()
        vyvod = [*step]
        cur.execute(f"""delete from students where id = {y}""")
        x = 0
        while 6 != x:
            print("""Что вы хотите изменить?
        1. Имя
        2. Фамилию
        3. Почту
        4. Номер телефона
        5. Поток
        6. Выход
        """)
            x = printy.vybor()
            if x == 1:
                vyvod[1] = printy.text('новое имя')
            elif x == 2:
                vyvod[2] = printy.text('новую фамилию')
            elif x == 3:
                vyvod[3] = printy.text('новую почту')
            elif x == 4:
                vyvod[4] = printy.text('новый номер телефона')
            elif x == 5:
                vyvod[0] = printy.integ('id потока')
        add_inf.add_student(vyvod)


def red_stream():
    read.stc()
    y = printy.id()
    con = sqlite3.connect('school_base.db')
    cur = con.cursor()
    with con:
        cur.execute(f"""select teacher_id, number, date_start, date_finish
        from streams where id = {y};""")
        step = cur.fetchone()
        vyvod = [*step]
        cur.execute(f"""delete from streams where id = {y};""")
        x = 0
        print("""Что вы хотите изменить?
        1. Номер потока
        2. Дату начала
        3. Дату окончания
        4. Преподователь
        5. Выход
        """)
        x = printy.vybor()
        while 5 != x:
            if x == 1:
                vyvod[1] = printy.text('новый номер потока')
            elif x == 2:
                vyvod[2] = printy.text('дату начала курса')
            elif x == 3:
                vyvod[3] = printy.text('дату окнчания курса')
            elif x == 4:
                vyvod[0] = printy.integ('id преподователя')
        add_inf.add_teacher(vyvod)


def red_course():
    read.ci()
    deli.del_course()
    complex.in_course()
    # y = printy.id()
    # con = sqlite3.connect('school_base.db')
    # cur = con.cursor()
    # with con:
    #     cur.execute(f"""select course_name from courses where id = {y};""")
    #     step = cur.fetchone()
    #     vyvod = [*step]
    #     cur.execute(f"""delete from Course where id = {y};""")
    #     x = 0
    #     print("""Что вы хотите изменить?
    #     1. Название курса
    #     2. Выход
    #     """)
    #     x = printy.vybor()
    #     while 2 != x:
    #         if x == 1:
    #             vyvod[0] = printy.text('новое название курса')
    # add_inf.add_teacher(vyvod)
