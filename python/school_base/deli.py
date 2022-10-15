import printy
import sqlite3


def del_teacher():
    y = printy.id()
    con = sqlite3.connect('school_base.db')
    cur = con.cursor()
    with con:
        cur.execute(f"""delete from teachers where id ={y};""")
    printy.delisey()


def del_student():
    y = printy.id()
    con = sqlite3.connect('school_base.db')
    cur = con.cursor()
    with con:
        cur.execute(f"""delete from students where id ={y};""")
    printy.delisey()


def del_stream():
    y = printy.id()
    con = sqlite3.connect('school_base.db')
    cur = con.cursor()
    with con:
        cur.execute(f"""delete from streams where id ={y};""")
    printy.delisey()


def del_course():
    y = printy.id()
    con = sqlite3.connect('school_base.db')
    cur = con.cursor()
    with con:
        cur.execute(f"""delete from courses where id ={y};""")
    printy.delisey()
