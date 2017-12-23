# attrgetter()
import operator

class Student(object):
    def __init__(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks

    def __str__(self):
        return '%s has marks %s' % (self.name, self.marks)


# to find the students with the highest marks
students = [Student(0, 'Foo', 30), Student(1, 'Bar', 95), Student(2, 'Baz', 80)]
best_student = max(students, key=operator.attrgetter('marks'))  # don't forget the quotes
print(best_student)

# to get the id of an object
f = operator.attrgetter('id')
Student3 = Student(2, 'Baz', 80)
print(f(Student3))  # >>> 2

import datetime

date1 = datetime.date(2017, 11, 26)
date2 = datetime.date(1986, 6, 7)
print(date1.year)  # >>> 2017
print(date2.day)  # >>> 7

yr = operator.attrgetter('year')
print(yr(date1))  # >>> 2017
print(yr(date2))  # >>> 1986



# itemgetter

import operator
import itertools

d1={'name':'AAA','age':18,'country':'China'}
d2={'name':'BBB','age':19,'country':'USA'}
d3={'name':'CCC','age':20,'country':'JP'}
d4={'name':'DDD','age':21,'country':'USA'}
d5={'name':'EEE','age':22,'country':'USA'}
d6={'name':'FFF','age':23,'country':'China'}
lst=[d1,d2,d3,d4,d5,d6]

# 利用itemgetter来排序
lst.sort(key=operator.itemgetter('country'))

# 用于针对dict中一个item的数值作为keyword, 比如找出最大值
print(max(lst, key=operator.itemgetter('age')))
print()

# 用于grouby中分组的keyword:
lstg = itertools.groupby(lst, operator.itemgetter('country'))
#lstg = itertools.groupby(lst,key=lambda x:x['country']) 等同于使用itemgetter()
for key,value_group in lstg:
    print(list(value_group))


# 这些项可以是操作数的__getitem__()方法接受的任何类型。字典接受任何哈希值。列表，元组和字符串接受索引或切片
import operator
s = 'ABCDEFG'
print(operator.itemgetter(1)(s))  # >>> 'B'
print(operator.itemgetter(1,3,5)(s))  # >>> ('B', 'D', 'F')
print(operator.itemgetter(slice(2,None))(s))  # >>> 'CDEFG'

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(operator.itemgetter(1)(l))  # >>> 'b'
print(operator.itemgetter(1,3,5)(l))  # >>> ('b', 'd', 'f')
print(operator.itemgetter(slice(2,None))(l))  # >>> ['c', 'd', 'e', 'f', 'g']


# 使用itemgetter()从元组记录中检索特定字段
import operator
inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
getcount = operator.itemgetter(1)


# 去出元组中的第1项
print(list(map(getcount, inventory)))  # >>> [3, 2, 5, 1]
print(list(map(lambda x:x[1], inventory)))

# 根据其中一项值来分组(还是使用key)
print(sorted(inventory, key=getcount)) # >>> [('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)]
