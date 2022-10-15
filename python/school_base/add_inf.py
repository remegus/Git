import sqlite3
import printy


def add_course(new_course):
    con = sqlite3.connect('school_base.db')
    with con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO Courses(Course_Name) VALUES(?);", new_course)
        printy.seyf()


def add_teacher(new_teacher):
    con = sqlite3.connect('school_base.db')
    with con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO Teachers(Course_id, First_Name, Last_Name, Mail, Number_Phone) VALUES(?, ?, ?, ?, ?);", new_teacher)
        printy.seyf()


def add_stream(new_stream):
    con = sqlite3.connect('school_base.db')
    with con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO Streams(Teacher_id, Number, Date_start, Date_finish) VALUES(?, ?, ?, ?);", new_stream)
        printy.seyf()


def add_student(new_student):
    con = sqlite3.connect('school_base.db')
    with con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO Students(Stream_id, S_First_Name, S_Last_Name, S_Mail, S_Number_Phone) VALUES(?, ?, ?, ?, ?);", new_student)
        printy.seyf()
