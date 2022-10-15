import sqlite3


def add_table():
    con = sqlite3.connect('school_base.db')
    with con:
        cur = con.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS Courses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Course_Name TEXT)
            ;""")

        cur.execute("""CREATE TABLE IF NOT EXISTS Teachers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Course_id INTEGER,
            First_Name TEXT,
            Last_Name TEXT,
            Mail TEXT,
            Number_Phone INTEGER)
            ;""")

        cur.execute("""CREATE TABLE IF NOT EXISTS Streams(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Teacher_id INTEGER,
            Number TEXT UNIQUE,
            Student_Amount INTEGER,
            Date_Start TEXT,
            Date_Finish TEXT)
            ;""")

        cur.execute("""CREATE TABLE IF NOT EXISTS Students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Stream_id INTEGER,
            S_First_Name TEXT,
            S_Last_Name TEXT,
            S_Mail TEXT,
            S_Number_Phone INTEGER)
            ;""")
