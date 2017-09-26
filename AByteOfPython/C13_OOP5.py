class SchoolMember:
    """学校全体成员"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        print('Name: {}, Age: {}'.format(self.name, self.age), end=", ")

class Teacher(SchoolMember):    # ----这里就是创造subclass
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: ${}'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: {}'.format(self.marks))

t1 = Teacher('Karen Schaich', 55, 90000)
s1 = Student('Denis Xie', 28, 'B-')
t2 = Teacher('Kit Yam', 60, 125000)
s2 = Student('Cindy Tian', 29, 'A')

print()
members = [t1, t2, s1, s2]
for member in members:
    member.tell()
