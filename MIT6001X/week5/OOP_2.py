# An extended example
# About people
# Start with Person object
import datetime

print()
class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
    def getLasstName(self):
        return self.lastName
    def __str__(self):
        return str(self.name)
    __repr__ = __str__  # this is added to make print simpler when called in a list

    def setBirthday(self, month, day, year):
        self.birthday = datetime.date(year, month, day)
    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    def __lt__(self, other):  # sort must be build on a system that allow comparison
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

p1 = Person('Mark Zuckerberg')
p1.setBirthday(5, 14, 1984)
p2 = Person('Drew Houston')
p2.setBirthday(3, 4, 1983)
p3 = Person('Bill Gates')
p3.setBirthday(10, 28, 1955)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')
personList = [p1, p2, p3, p4, p5]

print(p1.birthday)

print(p1)  # >>> Mark Zuckerberg
personList.sort()  # >>> this works because we defined __lt__ method, and it will sort by lastName
print(personList)  # >>> [Andrew Gates, Bill Gates, Drew Houston, Steve Wozniak, Mark Zuckerberg]

print()
class MITPerson(Person):
    nextIdNum = 0  # next ID number to assign
    def __init__(self, name):
        Person.__init__(self, name)  # initialize Person
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    def __str__(self):
        return self.name
    def getIdNum(self):
        return self.idNum

    # sorting by ID number not name
    def __lt__(self, other):
        return self.idNum < other.idNum

    def speak(self, utterance):
        return self.name + ' says: ' + utterance

m1 = MITPerson('Denis Xie')
print(m1.speak('how are you'))
m2 = MITPerson('Cindy Tian')
m3 = MITPerson('Adrienne Xie')

print(m1.getIdNum(), m2.getIdNum(), m3.getIdNum())
# >>> 0 1 2
lst = [m2, m1, m3]
lst.sort()
print(lst)  # >>> ['Denis Xie', 'Cindy Tian', 'Adrienne Xie']  # by ID

# print(denis < p4)  # denis.__lt__(p4)
# >>> AttributeError: 'Person' object has no attribute 'idNum'
print(p4 < m1)    # p4.__lt__(denis)
# >>> True   # this calls Person's method, compare by last name
# Whoever got called first, the method from that class is used



# create a further subclass of undergraduates and graduate student of MIT
print()

class Student(MITPerson):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year
    def speak(self, utterance):
        return MITPerson.speak(self, 'Dude, ' + utterance)

class UG(Student):  # UG as undergraduates
    pass

class Grad(Student):
    pass

class TransferStudent(Student):  # this caused a problem of rewriting the isStudent() method.
    pass
# a better way is to create a student(MITPerson), and all UG, Grads, TransferStudent inherit from there.

def isStudent(obj):
    return isinstance(obj, Student)  # so the method can be built on one superclass

s1 = UG('Denis Xie', 2008)
s2 = UG('Cindy Tian', 2007)
s3 = UG('Adrienne Xie', 2035)
s4 = UG('Fan Chen', 1978)

print(s1)  # >>> Denis Xie
print(s1.getClass())  # >>> 2008
print(s1.speak("What's up"))  # >>> Xie says: Dude, What's up

print(s1, s1.getIdNum(), s2, s2.getIdNum())  # >>> Denis Xie 3 Cindy Tian 4
lst = [s2, s4, s1, s3]
lst.sort()
print(lst)  # >>> ['Denis Xie', 'Cindy Tian', 'Adrienne Xie', 'Fan Chen']  # by ID



# create a professor class
print()
class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department
    def speak(self, utterance):
        new = 'In course ' + self.department + ' we say '
        return MITPerson.speak(self, new + utterance)
    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)

prof1 = Professor('Denis Xie', 'Food Science')
print(prof1.speak('Hello world'))
print(prof1.lecture('Organic Chemistry'))




# Another example class (grade book)
# build a data structure that can hold grades for students
# gather together data and procedures for dealing with them in a single structure
# so that the code can be used without knowing internal details
class Grades(object):
    """A mapping from students to a list of grades"""
    def __init__(self):
        """create empty grade book"""
        self.students = []
        self.grades = {}
        self.isSorted = True  # True if self.students is sorted
    def addStudent(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
    def addGrade(self, student, grade):
        """Assumes: grade is a float
           Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')
    def getGrades(self, student):
        """Return a list of grades for student"""
        try:
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')
    # def allStudents(self):
    #     """Return a list of students (sorted and copied) in the grade book"""
    #     if not self.isSorted:
    #         self.students.sort()
    #         self.isSorted = True
    #     return self.students
    def allStudents(self):  # new version by using generator
        """Return a list of students (sorted and copied) in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s

def gradeReport(course):  # a function to export a report for grades of a course
    """Assumes course ia of type grades"""
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s mean grade is ' + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)

MIT6001X = Grades()
studenList = [s2, s1, s3]  # use previous UG class example list
# [Cindy Tian, Fan Chen, Denis Xie, Adrienne Xie]


for i in studenList:
    MIT6001X.addStudent(i)
print(MIT6001X.allStudents())
# >>> [Denis Xie, Cindy Tian, Adrienne Xie, Fan Chen]
# >>> <generator object genTest at 0x104532db0>  # after using generator
k = MIT6001X.allStudents()
print(next(k))  # >>> Denis Xie
print(next(k))  # >>> Cindy Tian
print(next(k))  # >>> Adrienne Xie


MIT6001X.addGrade(s2, 75)
MIT6001X.addGrade(s2, 70)
MIT6001X.addGrade(s2, 70)
MIT6001X.addGrade(s2, 95)

MIT6001X.addGrade(s1, 91)
MIT6001X.addGrade(s1, 92)
MIT6001X.addGrade(s1, 88)
MIT6001X.addGrade(s1, 99)

MIT6001X.addGrade(s3, 59)
MIT6001X.addGrade(s3, 61)
MIT6001X.addGrade(s3, 59)
MIT6001X.addGrade(s3, 68)

print(MIT6001X.getGrades(s1))  # >>> [91, 92, 88, 99]
print(gradeReport(MIT6001X))
# >>>
# Denis Xie's mean grade is 90.0
# Cindy Tian's mean grade is 85.0
# Adrienne Xie's mean grade is 59.0
# Fan Chen's mean grade is 75.0

print(MIT6001X.grades)  # not encouraged as it exposes the attributes
# >>> {4: [75, 70, 70, 95], 3: [91, 92, 88, 99], 5: [59, 61, 59, 68]}



# introduce generator
def genTest():
    yield 1
    yield 2

k = genTest()
print(k)
for i in k:
    print(i)
# >>>
# 1
# 2
for i in k:
    print(i)
# >>> the generator is now empty, shows nothing as output

# use generator in fibonacci function
def genFib():  # this created a generator for fibonacci numbers
    index = 0
    a, b = 0, 1
    yield a
    yield b
    while True:
        next = a + b
        yield next
        a, b = b, next

# print a list of any length for fibonacci numbers
for n in genFib():
    print(n)
    if n >= 13:
        break
