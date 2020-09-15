#! python3
#This is a sample script


class Student:
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def do_home_work(self, time):
        if self.grade > 3 and time > 2:
            return True
        elif self.grade < 3 and time > 0.5:
            return True
        else:
            return False

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def evaluate(self, result=True):
        if result:
            return "You are doing well."
        else:
            return "It's not OK."

kid_a = Student('A', 5, 'math')
teach_x = Teacher('X', 'math')
teacher_said = teach_x.evaluate(kid_a.do_home_work(2))
print('Teacher {0} said: {1}, {2}'.format(teach_x.name, kid_a.name, teacher_said))

kid_b = Student('B', 5, 'math')
teach_y = Teacher('Y', 'math')
teacher_said = teach_y.evaluate(kid_b.do_home_work(3))
print('Teacher {0} said: {1}, {2}'.format(teach_y.name, kid_b.name, teacher_said))

