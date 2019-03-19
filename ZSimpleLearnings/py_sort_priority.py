# why python __lt__ has higher priority than __gt__?

class Person(object):
    id = 0
    def __init__(self, name):
        self.name = name
        self.id = Person.id
        Person.id += 1

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.id < other.id

class SubPerson(Person):
    def __init__(self, name):
        Person.__init__(self, name)
    def __gt__(self, other):
        return self.name > other.name

s1 = SubPerson('AAA'); s1.id = 14
s2 = SubPerson('BBB'); s2.id = 12
s3 = SubPerson('CCC'); s3.id = 11
s4 = SubPerson('DDD'); s4.id = 13

lst = [s2, s1, s4, s3]
lst.sort()
print([i.__str__() for i in lst])  # >>> ['CCC', 'BBB', 'DDD', 'AAA']  # still sort by id in superclass

# Observation:
# __gt__ will work solo without __lt__
# __lt__ has higher priority, even from superclass


# STOF: https://stackoverflow.com/q/48313301/8435726
# conclusion: always sort based on __lt__ only, __gt__ will work solo by side-effect
#  __gt__ solo is a side effect from a reflective test application:
# checking the __gt__ when the __lt__ is missing in comparison
