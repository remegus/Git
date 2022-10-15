import printy
import add_inf
import read


def redact_in(new_line):
    new_line = tuple(new_line)
    print(new_line)
    return new_line


def in_teacher():
    read.ci()
    new_line = []
    new_line.append(printy.integ('id курса'))
    new_line.append(printy.text('имя'))
    new_line.append(printy.text('фамилию'))
    new_line.append(printy.text('почту'))
    new_line.append(printy.integ('номер телефона'))
    redact_in(new_line)
    add_inf.add_teacher(new_line)


def in_course():
    read.ci()
    new_line = []
    new_line.append(printy.text('название курса'))
    redact_in(new_line)
    add_inf.add_course(new_line)


def in_stream():
    read.tc()
    new_line = []
    new_line.append(printy.integ('id учителя'))
    read.stc()
    new_line.append(printy.text('номер потока'))
    new_line.append(printy.text('дата начала обучения потока'))
    new_line.append(printy.text('дата окончания обучения потока'))
    redact_in(new_line)
    add_inf.add_stream(new_line)


def in_student():
    read.stc()
    new_line = []
    new_line.append(printy.integ('id потока'))
    new_line.append(printy.text('имя'))
    new_line.append(printy.text('фамилия'))
    new_line.append(printy.text('почта'))
    new_line.append(printy.integ('номер телефона'))
    redact_in(new_line)
    add_inf.add_student(new_line)
