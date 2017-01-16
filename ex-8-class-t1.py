# use python 3.4 for below example
# due to print function in python 3.4
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print ("{}: {}".format(self.name, self.score))

    @classmethod
    def print_cls(cls):
        print ("{}".format(cls))

    @staticmethod
    def print_sta(x):
        print ("{}".format(x))        

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

bart.print_score()
lisa.print_score()

bart.print_cls()
Student.print_cls()

bart.print_sta(3)
Student.print_sta(4)
