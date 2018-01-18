class Person(object):
    id = 0
    def __init__(self, name):
        self.name = name
        self.id = Person.id
        Person.id += 1

    def __str__(self):
        return self.name

    def __gt__(self, other):
        return self.id > other.id


p1 = Person('AAA')
p2 = Person('BBB')
p3 = Person('CCC')
p4 = Person('DDD')

lst = [p2, p3, p1, p4]
lst.sort()
print([i.__str__() for i in lst])  # >>> ['AAA', 'BBB', 'CCC', 'DDD']


class SubPerson(Person):
    def __init__(self, name):
        Person.__init__(self, name)
    def __gt__(self, other):
        return self.id > other.id

s1 = SubPerson('WWW'); s1.id = 14
s2 = SubPerson('XXX'); s2.id = 12
s3 = SubPerson('YYY'); s3.id = 11
s4 = SubPerson('ZZZ'); s4.id = 13
lst2 = [s2, s1, s4, s3]
lst2.sort()
print([i.__str__() for i in lst2])  # >>> ['YYY', 'XXX', 'ZZZ', 'WWW']


# https://stackoverflow.com/questions/48313301/python-sort-has-higher-priority-for-lt-than-gt?noredirect=1#48313338
# conclusion: sort based on __lt__ only.
# __gt__ solo is a side effect from a reflective test application:
# checking the __gt__ when the __lt__ is missing in comparison


