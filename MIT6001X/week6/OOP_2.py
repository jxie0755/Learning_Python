# An extended example
# About people
# Start with Person object
import datetime
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
for i in lst:
    print(i)

