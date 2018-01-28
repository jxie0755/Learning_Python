# operator module
# https://docs.python.org/3/library/operator.html#module-operator

import operator


print()
print('operator.attrgetter(attr)')
print('operator.attrgetter(*attrs)')

# 返回从其操作数获取attr的可调用对象。如果请求多个属性，则返回一个属性元组。属性名称也可以包含点

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



print()
print('operator.itemgetter(item)')
print('operator.itemgetter(*items)')

# 返回使用操作数的__getitem__()方法从其操作数获取项的可调用对象。如果指定了多个项，则返回查找值的元组。

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


# operator.lt(a, b)  ==   a < b
# operator.le(a, b)  ==   a <= b
# operator.eq(a, b)  ==   a == b
# operator.ne(a, b)  ==   a != b
# operator.ge(a, b)  ==   a >= b
# operator.gt(a, b)  ==   a > b

# operator.__lt__(a, b)
# operator.__le__(a, b)
# operator.__eq__(a, b)
# operator.__ne__(a, b)
# operator.__ge__(a, b)
# operator.__gt__(a, b)

# 逻辑操作也通常适用于所有对象，并支持真值测试，身份测试和布尔运算
# 这些带双__前后的method很多都可以用于定义新的类方法(OOP环境)

# operator.not_(obj)
# operator.__not__(obj)
# 返回not obj。（请注意，对象实例没有__not__()方法；只有解释器核定义了此操作。结果受到__bool__()和__len__()方法的影响。）

# operator.truth(obj)
# 如果obj为真，则返回True，否则返回False。这相当于使用bool构造函数。

# operator.is_(a, b)
# 返回a 是 b。测试对象标识。

# operator.is_not(a, b)
# 返回a 是 不是 b。测试对象标识。
print(operator.is_not(6, 6))

# 数学和按位操作是最多的：

# operator.abs(obj)
# operator.__abs__(obj)
# 返回obj的绝对值

# operator.add(a, b)
# operator.__add__(a, b)
# 返回a + b，对于a和b t5 >数字

# operator.and_(a, b)
# operator.__and__(a, b)
# 返回按位和a和b
print(operator.and_(True, True))

# operator.floordiv(a, b)
# operator.__floordiv__(a, b)
# 返回a // b。

# operator.index(a)
# operator.__index__(a)
# 返回a转换为整数。等同于a.__index__()

# operator.inv(obj)
# operator.invert(obj)
# operator.__inv__(obj)
# operator.__invert__(obj)
# 返回数字obj的按位逆。这相当于~obj
print(operator.inv(123))  # >>> -124

# operator.lshift(a, b)
# operator.__lshift__(a, b)
# 返回a向左移动b

# operator.mod(a, b)
# operator.__mod__(a, b)
# 返回a % b

# operator.mul(a, b)
# operator.__mul__(a, b)
# 返回a * b，对于a和b t5 >数字

# operator.matmul(a, b)
# operator.__matmul__(a, b)
# 返回a @ b

# operator.neg(obj)
# operator.__neg__(obj)
# 返回obj否定（-obj）。

# operator.or_(a, b)
# operator.__or__(a, b)
# 返回按位或a和b。

# operator.pos(obj)
# operator.__pos__(obj)
# 返回obj正（+obj）。

# operator.pow(a, b)
# operator.__pow__(a, b)
# 对于a和b，返回a ** b t5>数字。

# operator.rshift(a, b)
# operator.__rshift__(a, b)
# 返回a向右移动b。

# operator.sub(a, b)
# operator.__sub__(a, b)
# 返回a - b。

# operator.truediv(a, b)
# operator.__truediv__(a, b)
# 返回a / b其中2/3为.66而不是0。这也被称为“真正的”分裂。

# operator.xor(a, b)
# operator.__xor__(a, b)
# 返回a和b的逐位异或。

# 使用序列（其中一些与映射）的操作包括：

# operator.concat(a, b)
# operator.__concat__(a, b)
# 对于a和b返回a + b序列。

# operator.contains(a, b)
# operator.__contains__(a, b)
# 返回 t> a中的测试结果b 。注意反向操作数。

# operator.countOf(a, b)
# 返回a中b的出现次数。

# operator.delitem(a, b)
# operator.__delitem__(a, b)
# 删除索引b处a的值。

# operator.getitem(a, b)
# operator.__getitem__(a, b)
# 返回a在索引b的值。

# operator.indexOf(a, b)
# 返回a中b的第一个出现的索引。

# operator.setitem(a, b, c)
# operator.__setitem__(a, b, c)
# 将索引b处的a值设置为c。

# operator.length_hint(obj, default=0)
# 返回对象o的估计长度。首先尝试返回其实际长度，然后使用object.__length_hint__()进行估计，最后返回默认值。

# operator.iadd(a, b)
# operator.__iadd__(a, b)
# a = iadd(a, b) is equivalent to a += b.

# operator.iand(a, b)
# 操作符。 __ iand __ （ a，b ） t5 >
# a = iand(a, b) is equivalent to a &= b.

# operator.iconcat(a, b)
# operator.__iconcat__(a, b)
# a = iconcat(a, b) is equivalent to a += b for a and b sequences.

# operator.ifloordiv(a, b)
# operator.__ifloordiv__(a, b)
# a = ifloordiv(a, b) is equivalent to a //= b.

# operator.ilshift(a, b)
# operator.__ilshift__(a, b)
# a = ilshift(a, b) is equivalent to a <<= b.

# operator.imod(a, b)
# operator.__imod__(a, b)
# a = imod(a, b) is equivalent to a %= b.

# operator.imul(a, b)
# operator.__imul__(a, b)
# a = imul(a, b) is equivalent to a *= b.

# operator.imatmul(a, b)
# operator.__imatmul__(a, b)
# a = imatmul(a, b) is equivalent to a @= b.

# operator.ior(a, b)
# operator.__ior__(a, b)
# a = ior(a, b) is equivalent to a |= b.

# operator.ipow(a, b)
# operator.__ipow__(a, b)
# a = ipow(a, b) is equivalent to a **= b.

# operator.irshift(a, b)
# operator.__irshift__(a, b)
# a = irshift(a, b) is equivalent to a >>= b.

# operator.isub(a, b)
# operator.__isub__(a, b)
# a = isub(a, b) is equivalent to a -= b.

# operator.itruediv(a, b)
# operator.__itruediv__(a, b)
# a = itruediv(a, b) is equivalent to a /= b.

# operator.ixor(a, b)
# operator.__ixor__(a, b)
# a = ixor(a, b) is equivalent to a ^= b.
