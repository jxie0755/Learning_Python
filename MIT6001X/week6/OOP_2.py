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
        return self.name

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
p1.setBirthday(5, 14, 84)
p2 = Person('Drew Houston')
p2.setBirthday(3, 4, 83)
p3 = Person('Bill Gates')
p3.setBirthday(10, 28, 55)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')
personList = [p1, p2, p3, p4, p5]

print(p1)  # >>> Mark Zuckerberg
personList.sort()  # >>> this works because we defined __lt__ method, and it will sort by lastName
for e in personList:
    print(e)
# >>>
# Andrew Gates
# Bill Gates
# Drew Houston
# Steve Wozniak
# Mark Zuckerberg

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
        return self.getLasstName() + ' says: ' + utterance

denis = MITPerson('Denis Xie')
print(denis.speak('how are you'))
cindy = MITPerson('Cindy Tian')
adrienne = MITPerson('Adrienne Xie')

print(denis.getIdNum(), cindy.getIdNum(), adrienne.getIdNum())
# >>> 0 1 2
lst = [cindy, denis, adrienne]
lst.sort()
print([i.__str__() for i in lst])  # >>> ['Denis Xie', 'Cindy Tian', 'Adrienne Xie']  # by ID

# print(denis < p4)  # denis.__lt__(p4)
# >>> AttributeError: 'Person' object has no attribute 'idNum'
print(p4 < denis)    # p4.__lt__(denis)
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
print([i.__str__() for i in lst])  # >>> ['Denis Xie', 'Cindy Tian', 'Adrienne Xie', 'Fan Chen']  # by ID

