import sqlite3


def stc():
    """
    поток -> учитель -> курс
    """
    vyvod = []
    con = sqlite3.connect('school_base.db')
    with con:
        cur = con.cursor()
        rew = """SELECT streams.id, Streams.Number, Teachers.Last_name, Teachers.First_Name, 
        Courses.Course_Name FROM Streams 
        LEFT JOIN Teachers ON Streams.Teacher_id = Teachers.id
        LEFT JOIN Courses ON Teachers.Course_id = Courses.id"""
        for step in cur.execute(rew):
            print(step)
            step = [*step]
            step.pop(0)
            vyvod.append(step)
        return vyvod


def tc():
    """
    Учитель -> курс
    """
    vyvod = []
    con = sqlite3.connect('school_base.db')
    with con:
        cur = con.cursor()
        rew = """SELECT Teachers.id, Teachers.Last_name, Teachers.First_Name, 
        Courses.Course_Name FROM Teachers 
        LEFT JOIN Courses ON Teachers.Course_id = Courses.id"""
        for step in cur.execute(rew):
            print(step)
            step = [*step]
            step.pop(0)
            vyvod.append(step)
        return vyvod


def ss():
    """
    студент -> поток
    """
    con = sqlite3.connect('school_base.db')
    with con:
        cur = con.cursor()
        vyvod = []
        rew = """select students.id, students.s_last_name, students.s_first_name,
        s_mail, s_number_phone, streams.number from students 
        left join streams on stream_id = streams.id
        left join teachers on streams.teacher_id = teachers.id"""
        for step in cur.execute(rew):
            print(step)
            step = [*step]
            step.pop(0)
            vyvod.append(step)
        return vyvod


def all():
    """
    студент -> поток -> учитель -> курс
    """
    con = sqlite3.connect('school_base.db')
    with con:
        cur = con.cursor()
        vyvod = []
        rew = """select students.id, students.s_last_name, students.s_first_name,
        s_mail, s_number_phone, 
        streams.number, teachers.id, teachers.first_name, teachers.last_name,
        courses.id, courses.course_name from students 
        left join streams on stream_id = streams.id
        left join teachers on streams.teacher_id = teachers.id
        left join courses on teachers.course_id = courses.id"""
        for step in cur.execute(rew):
            print(step)
            step = [*step]
            step.pop(0)
            vyvod.append(step)
        return vyvod


def ci():
    """
    Курсы
    """
    vyvod = []
    con = sqlite3.connect('school_base.db')
    with con:
        cur = con.cursor()
        for step in cur.execute('select id, course_name from courses'):
            print(step)
            step = [*step]
            step.pop(0)
            vyvod.append(step)
        return vyvod


# stc()
# tc()
# ci()
# ss()
# all()
