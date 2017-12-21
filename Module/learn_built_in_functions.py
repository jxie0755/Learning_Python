# A try out for all the built-in functions in python

print(1)
print('abs()')
print(abs(-4))  # >>> 4
# absolute value
# argument: int and float
# return the


print(2)
print('all()')
print(all([0, 4]))  # >>> False
print(all([]))  # >>> True
# argument: iterable objects
# return True if all elements of the iterable are true
# if the iterable is empty, return True


print(3)
print('any()')
print(any([0, 4]))  # >>> True
# argument: iterable objects
# return True if any elements of the iterable are true
# if the iterable is empty, return True


print(4)
print('ascii()')
print(ascii('ö'))  # >>> xf6n
print('Pyth\xf6n')  # >>>Pythön
# argument: an object
# return a string containing a printable representation of an object, but escape the non-ASCII characters in the string returned by repr() using \x, \u, \U escapes.
# For example, ö is changed to \xf6n, √ is changed to \u221a

print(5)
print('bin()')
print(bin(3))  # >>> 0b11
print(bin(-10))  # >>> -0b1010
print(format(10, 'b'))  # >>> 1010, this can remove the '0b'
# convert to binary number with a prefix '0b'
# argument: an integer number
# return the binary value


print(6)
print('bool()')
print(bool(0))  # >>> False
print(bool('0'))  # >>> True
print(bool(None))  # >>> False
print(bool([]))  # >>> False
# argument can be any object
# return True or False
# None，False，0, 0.0,空字符串'', 空元组(), 空列表[]， 空字典{} 这些算作False
# 其他皆为True


print(7)
print('bytearray()')
print(bytearray([0, 100, 255]))  # >>> bytearray(b'\x00d\xff')
print(bytearray(12))  # >>> bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
print(bytes([0, 100, 255]))  # >>> b'\x00d\xff'
print(bytes(12))  # >>> b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
# 暂时不理解


print(8)
print('bytes()')
# 返回一个新的字节对象，是一个在 0<= x < 256之间的不可变的整数序列。 
# bytes 是 bytearray 的不可变版本 – 它具有同样的非改变性的方法和同样的索引和切片操作
# 因此，构造函数参数的解释与bytearray()相同。

print(9)
print('callable()')
print(callable(1))  # >>> False
print(callable(abs))  # >>> True, function is callable
print(callable([1, 2]))  # >>> True, function is callable
print(callable(zip()))  # >>> False, if with '()'
# argument: any object
# return True if it is callable, otherwise False


print(10)
print('chr()')
print(chr(97))  # >>> a, refer the ascii table
print(ord('a'))  # >>> 97, the inverse function of chr
print(chr(127))  # >>> 
# The valid range for the argument is from 0 through 1,114,111
# ascii table is from 0 to 127
# return the character accordingly


print(11)
print('classmethod()')
print(classmethod(abs(5)))
# 将函数包装成类方法
# 暂时不理解


print(12)
print('compile()')
# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
# 暂时不理解


print(13)
print('complex()')
print(complex('1+2j'))
# 返回值形式为real + imag * 1j的复数，或将字符串或数字转换为复数
# does not allow white space in the string ('1 + 2j') will raise error
# 暂时不理解


print(14)
print('delattr()')
# delattr(object, 's')
# 这个函数和setattr()有关。参数是一个对象和一个字符串。
# 字符串必须是对象的某个属性的名字。只要对象允许，这个函数删除该名字对应的属性。
# delattr(x, 'foobar')等同于del x.foobar。
# 暂时不理解


print(15)
print('dict()')
print(dict(zip([1, 2, 3], ['a', 'b', 'c'])))
# create a dictionary


print(16)
print('dir()')
print(dir())
# 如果没有参数，返回当前本地作用域内的名字列表。
# 如果有参数，尝试返回参数所指明对象的合法属性的列表。


print(17)
print('divmod()')
print(divmod(7, 2))  # >>> (3, 1) return a tuple
for i in divmod(7, 2):
    print(i)
# Take two (non complex) numbers as arguments
# return a pair of numbers consisting of their quotient and remainder


print(18)
print('enumerate()')
l = ['apple', 'banana', 'pear', 'mango']
print(list(enumerate(l, start=1)))
# >>> [(1, 'apple'), (2, 'banana'), (3, 'pear'), (4, 'mango')]
print(dict(enumerate(l, start=1)))
# >>> {1: 'apple', 2: 'banana', 3: 'pear', 4: 'mango'}
# argument: iterable object, default start with 0.
# return a paired value, but needs a container (list, dict, etc)


print(19)
print('eval()')
# eval(expression, globals=None, locals=None)
print('see in ZSimpleLearnings/python_eval.py')
print('AVOID USING!!!!')


print(20)
print('exec()')
# exec(object[, globals[, locals]])
print('see in ZSimpleLearnings/python_eval.py')
print('AVOID USING!!!!')


print(21)
print('filter()')
print('see in ZSimpleLearnings/lambda_map_filter_reduce.py')


print(22)
print('float()')
print(float(25))  # >>> 25.0
print(float('-25'))  # >>> -25.0
# convert an int or number in string to a float number


print(23)
print('format()')
# 'd' for integer
print(format(123, "d"))  # must be integer
# 'f' for float arguments
print(format(123, "f"))  # 总是六位小数
# 'b' for binary format
print(format(12, "b"))
# d, f and b are type
# integer
print(format(1234, "*>+7,d"))
# float number
print(format(123.4567, "^-09.3f"))  # 暂时不理解

# 四舍五入与round类似
print(format(1.5, '0.0f'))  # >>> 2
print(format(2.5, '0.0f'))  # >>> 2
print(format(1.55, '0.1f'))  # >>> 1.6
print(format(2.55, '0.1f'))  # >>> 2.5


print(24)
print('frozenset()')
# print(frozenset([1, 2, 3]))
# 暂时不理解


print(25)
print('getattr()')
print('see in ZSimpleLearnings/python_getattr.py')


print(26)
print('globals()')
print(globals())
# returns the dict of the current module


print(27)
print('hasattr()')
# 参数是一个对象和一个字符串。如果字符串是对象的一个属性，则返回True，否则返回False。
# 它的实现是通过调用getattr(object, name)并查看它是否引发一个AttributeError
lst = [1,2,3]
print(hasattr(lst, 'append'))  # >>> True
print(hasattr(lst, 'insert'))  # >>> True

strin = 'abc'
print(hasattr(strin, 'isalpha'))  # >>> True
print(hasattr(strin, 'ascii_lowercase'))  # >>> False
import string
print(hasattr(string, 'ascii_lowercase'))  # >>> True
# 更多用于oop环境

print(28)
print('hash()')
# Hash values are just integers which are used to ~
# compare dictionary keys during a dictionary lookup quickly.
print(hash(181))
print(hash(181.23))
print(hash('Python'))
vowels = ('a', 'e', 'i', 'o', 'u')
print(hash(vowels))


print(29)
print('help()')
# help() returns the doc str
help(abs)
help(list)
# It's recommenced to try it in your interpreter when you need help to ~
# write Python program and use Python modules


print(30)
print('hex()')
# like bin, hex() returns an integer to hexadecimal number
# start with '0x'
print(hex(123456))
print(format(123456, 'x'))
# also use format 'x' to skip the '0x' prefix, use 'X' to upper the letters


print(31)
print('id()')
# id is very similar to hash, an identity of an object
print(id(5))


print(32)
print('input()')
# input()
# to have user input with a hint as the argument


print(33)
print('int()')
# int(x, base=10)
# don't forget that base can be changed from 2-36.
# base为0意味着完全解释为代码字面值
a = '142AB34'
print(int(a, base=16))  # >>> 21146420
b = '10101'
print(int(b, base=2))   # >>> 21

print(34)
print('isinstance(object, classinfo)')
# 如果object是clsaainfo的一个实例（或者是classinfo的直接、间接或虚拟子类的实例），那么则返回true。
# 如果对象不是给定类型的对象，则函数始终返回false
# 暂时不理解


print(35)
print('issubclass()')
# 如果 class 是classinfo的子类(直接、 间接或 虚拟) 则返回 true 。
# 一个类被认为是它自己的子类。classinfo可以是类对象的元组，这时classinfo中的每个类对象都会被检查。

print(36)
print('iter()')
# 返回一个迭代器对象

print(37)
print('len()')
# return length of a iterable


print(39)
print('list()')
# turn iterable into a list


print(39)
print('locals()')
# 暂时不理解

print(40)
print('map()')
print('see in ZSimpleLearnings/lambda_map_filter_reduce.py')

print(41, 43)
print('max() and min()')
print('see in ZSimpleLearnings/max_min.py')


print(42)
print('memoryview()')
# Return the object's memory address?
# memoryview: a bytes-like object is required, not 'str'
print(memoryview(b'abcde'))  # >>> <memory at 0x7f3271528048>
print(memoryview('abcde'.encode('utf-8')))  # >>> <memory at 0x7f3271528048>

print(44)
print('next()')
# consume the next item in an iterator
print('see in Module/learn_itertools.py')


print(45)
print('object()')
# oop 环境

print(46)
print('oct(x)')
# 将整数转换为八进制字符串。结果是一个合法的Python表达式。
print(oct(120))  # >>> 0o170  'o' means 八进制
print(oct(1999)) # >>> 0o3717


print(47)
print('open()')
print('see in ZSimpleLearnings/write_and_write_back.py')


print(48)
print('ord(c)')
# 给定一个表示一个Unicode字符的字符串，返回一个表示该字符的Unicode代码点的整数。
print(ord('a'))  # >>> 97
print(ord(' '))  # >>> 32
print(ord('#'))  # >>> 35
# refer ascii table (0-127)
# but also support more than 0-127
print(chr(1223))  # >>> Ӈ
print(ord('Ӈ'))   # >>> 1223
# The valid range for the argument is from 0 through 1,114,111


print(49)
print('pow(x, y[, z])')
# return x^y
# 如果提供z参数， 返回x^y再除以z的余数
print(pow(2, 3, 7))  # >>> 8 (2^3=8)
print(pow(2, 3, 7))  # >>> 1 (8//7=1, 余1)


print(50)
print('print()')
print('hello world')


print(51)
print('range(stop)')
print('range(start, stop[, step])')
print('well understood')


print(52)
print('property()')
# oop 环境

print(53)
print('repr(object)')
# 返回某个对象可打印形式的字符串。
a = [1,2,3]
print(repr(a))  # >>> [1, 2, 3]
print(a)

b = range(5)
print(repr(b))  # >>> range(0, 5)
print(b)

c = 'abcd'
print(repr(c))  # >>> 'abcd'   difference is that it will show ''
print(c)        # >>> abcd

import datetime
today = datetime.datetime.now()
# Prints readable format for date-time object
print(today)        # >>> 2017-12-21 20:12:24.180042
# prints the official format of date-time object
print(repr(today))  # >>> datetime.datetime(2017, 12, 21, 20, 12, 24, 180042)


print(54)
print('reversed(seq)')
# 返回一个反向iterator
a = [1,2,3]
print(list(reversed(a)))
print('see in ZSimpleLearnings/sort_vs_sorted_and_reverse.py')


print(55)
print('round(number[, ndigits])')
# 当一个值刚好在两个边界的中间的时候， round 函数返回离它最近的偶数。 
print(round(1.5, 0))  # >>> 2.0
print(round(2.5, 0))  # >>> 2.0
# 也就是说，对1.5或者2.5的舍入运算都会得到2。


print(56)
print('set([iterable])')
# create a set object

print(57)
print('setattr(object, name, value)')
# 它与getattr()相对应。参数是一个对象、一个字符串和一个任意值。
# 字符串可以是一个已存在属性的名字也可以是一个新属性的名字。
# 该函数将值赋值给属性，只要对象允许。


print(58)
print('slice()')
# slice a list
a = [1,2,3,4]
b = a[0:2]
print(b)  # >>> [1, 2]

print(59)
print('sorted()')
# sort from small to large (num, alpha)
print('see in ZSimpleLearnings/sort_vs_sorted_and_reverse.py')


print(60)
print('staticethod()')
# 返回function的一个静态方法。


print(61)
print('str()')
# turn object into a string version


print(62)
print('sum()')
# return the sum of an iterable
# 对于某些使用情况，有很好的替代sum()的方法。
# 连接字符串序列的首选快速方法是调用''.join(sequence)。


print(63)
print('super()')
# 返回一个代理对象，它委托方法给父类或者type的同级类。
# 这对于访问类中被覆盖的继承方法很有用。
# oop环境


print(64)
print('tuple()')
# create a tuple from an iterable


print(65)
print('type()')
# return the type of the object


print(66)
print('vars()')
print('see in ZSimpleLearnings/python_vars.py')


print(67)
print('zip()')
# very use full to link a group of arrays
print('see in ZSimpleLearnings/python_zip.py')


print(68)
print('__import__()')
# 用于import任何文件名
# surpose a file named 05_if1_guess_number.py, we want to import this file
mymodule = __import__('05_if1_guess_number')

