import sqlite3
import complex
import add_inf
import table

table.add_table()

Courses = [('python',),
           ('java',),
           ('enjener',),
           ('data sience',),
           ('linux',)]
for co in Courses:
    add_inf.add_course(co)

Teachers = [(1, 'Michael', 'Fox', 'ndgf', 45643),
            (2, 'Adam', 'Miller', 'dhdea', 5356),
            (3, 'Andrew', 'Peck', 'agsgg', 34563),
            (4, 'Curl', 'Shreder', 'dhdtgh', 364536),
            (5, 'Smit', 'Greck', 'dhdtgh', 364536),
            (4, 'James', 'Shroyer', 'dhdtgh', 364536),
            (5, 'Eric', 'Burger', 'wetthf', 465466)]
for te in Teachers:
    add_inf.add_teacher(te)


Streams = [(1, 'a20', '1.9.2020', '1.6.2023'),
           (2, 'b20', '1.9.2020', '1.6.2024'),
           (3, 'c20', '1.9.2020', '1.6.2023'),
           (4, 'd20', '1.9.2020', '1.6.2024'),
           (5, 'i20', '1.9.2020', '1.6.2024'),
           (6, 'f20', '1.9.2020', '1.6.2024'),
           (7, 'g20', '1.9.2020', '1.6.2024'),
           (3, 'j20', '1.9.2020', '1.6.2024'),
           (1, 'y20', '1.9.2020', '1.6.2024')]
for st in Streams:
    add_inf.add_stream(st)


Students = [(1, 'Руслан', 'Fox', 'ndgf', 5643),
            (2, 'Алексей', 'Miller', 'dhdea', 5356),
            (3, 'Павел', 'Peck', 'agsgg', 4563),
            (4, 'Анатолий', 'Peck', 'agsgg', 4563),
            (5, 'Антон', 'Peck', 'agsgg', 4563),
            (6, 'Андрей', 'Peck', 'agsgg', 4563),
            (7, 'Тимофей', 'Peck', 'agsgg', 4563),
            (8, 'Владимир', 'Peck', 'agsgg', 4563),
            (9, 'Дмитрий', 'Peck', 'agsgg', 4563),
            (1, 'Генадий', 'Peck', 'agsgg', 4563),
            (2, 'Илья', 'Shroyer', 'dhdtgh', 4536),
            (3, 'Сергей', 'Burger', 'wetthf', 5466)]
for sd in Students:
    add_inf.add_student(sd)
