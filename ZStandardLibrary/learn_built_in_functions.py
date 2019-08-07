"""
python 3.6 built-in functions
https://docs.python.org/3/library/functions.html#built-in-functions
"""

print("\n", 1)
print("abs(x)")
print(abs(-4))  # >>> 4
# absolute value
# argument: int and float
# return the


print("\n", 2)
print("all(iterable)")
print(all([0, 4]))  # >>> False
print(all([]))  # >>> True
# argument: iterable objects
# return True if all elements of the iterable are true
# if the iterable is empty, return True


print("\n", 3)
print("any(iterable)")
print(any([0, 4]))  # >>> True
# argument: iterable objects
# return True if any elements of the iterable are true
# if the iterable is empty, return True


print("\n", 4)
print("ascii(object)")
print(ascii("ö"))  # >>> xf6n
print("Pyth\xf6n")  # >>>Pythön
# argument: an object
# return a string containing a printable representation of an object, but escape the non-ASCII characters in the string returned by repr() using \x, \u, \U escapes.
# For example, ö is changed to \xf6n, √ is changed to \u221a

print("\n", 5)
print("bin(x)")
print(bin(3))  # >>> 0b11
print(bin(-10))  # >>> -0b1010
print(format(10, "b"))  # >>> 1010, this can remove the "0b"
# convert to binary number with a prefix "0b"
# argument: an integer number
# return the binary value

print("\n", 6)
print("class bool([x])")
print(bool(0))  # >>> False
print(bool("0"))  # >>> True
print(bool(None))  # >>> False
print(bool([]))  # >>> False
# argument can be any object
# return True or False
# None，False，0, 0.0,空字符串"", 空元组(), 空列表[]， 空字典{} 这些算作False
# 其他皆为True


print("\n", 7)
print("class bytearray([source[, encoding[, errors]]])")
print(bytearray([0, 100, 255]))  # >>> bytearray(b"\x00d\xff")
print(bytearray(12))  # >>> bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
print(bytes([0, 100, 255]))  # >>> b"\x00d\xff"
print(bytes(12))  # >>> b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"


print("\n", 8)
print("class bytes([source[, encoding[, errors]]])")
# 返回一个新的字节对象，是一个在 0<= x < 256之间的不可变的整数序列。
# bytes 是 bytearray 的不可变版本 – 它具有同样的非改变性的方法和同样的索引和切片操作
# 因此，构造函数参数的解释与bytearray()相同。


print("\n", 9)
print("callable(object)")
print(callable(1))  # >>> False
print(callable(abs))  # >>> True, function is callable
print(callable([1, 2]))  # >>> True, function is callable
print(callable(zip()))  # >>> False, if with "()"
# argument: any object
# return True if it is callable, otherwise False


print("\n", 10)
print("chr(i)")
print(chr(97))  # >>> a, refer the ascii table
print(ord("a"))  # >>> 97, the inverse function of chr
print(chr(127))  # >>> 
# The valid range for the argument is from 0 through 1,114,111
# ascii table is from 0 to 127
# return the character accordingly


print("\n", 11)
print("classmethod(function)")
print(classmethod(abs))
# 将函数包装成类方法
# oop环境


print("\n", 12)
print("compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)")
# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
# 暂时不理解


print("\n", 13)
print("class complex([real[, imag]])")
print(complex("1+2j"))
# 返回值形式为real + imag * 1j的复数，或将字符串或数字转换为复数
# does not allow white space in the string ("1 + 2j") will raise error
# 暂时不理解


print("\n", 14)
print("delattr(object, name)")
# delattr(object, "s")
# 这个函数和setattr()有关。参数是一个对象和一个字符串。
# 字符串必须是对象的某个属性的名字。只要对象允许，这个函数删除该名字对应的属性。
# delattr(x, "foobar")等同于del x.foobar。
# oop环境


print("\n", 15)
print("class dict(**kwarg)")
print("class dict(mapping, **kwarg)")
print("class dict(iterable, **kwarg)")
print(dict(zip([1, 2, 3], ["a", "b", "c"])))
# create a dictionary


print("\n", 16)
print("dir([object])")
print(dir())
# 如果没有参数，返回当前本地作用域内的名字列表。
# 如果有参数，尝试返回参数所指明对象的合法属性和方法的列表。


print("\n", 17)
print("divmod(a, b)")
print(divmod(7, 2))  # >>> (3, 1) return a tuple
for i in divmod(7, 2):
    print(i)
# Take two (non complex) numbers as arguments
# return a pair of numbers consisting of their quotient and remainder


print("\n", 18)
print("enumerate(iterable, start=0)")
l = ["apple", "banana", "pear", "mango"]
print(list(enumerate(l, start=1)))
# >>> [(1, "apple"), (2, "banana"), (3, "pear"), (4, "mango")]
print(dict(enumerate(l, start=1)))
# >>> {1: "apple", 2: "banana", 3: "pear", 4: "mango"}
# argument: iterable object, default start with 0.
# return a paired value, but needs a container (list, dict, etc)


print("\n", 19)
print("eval(expression, globals=None, locals=None)")
# eval(expression, globals=None, locals=None)
print("see in ZSimpleLearnings/py_eval_exec.py")
print("AVOID USING!!!!")


print("\n", 20)
print("exec(object[, globals[, locals]])")
# exec(object[, globals[, locals]])
print("see in ZSimpleLearnings/py_eval_exec.py")
print("AVOID USING!!!!")


print("\n", 21)
print("filter(function, iterable)")
print("see in ZSimpleLearnings/py_high_order_functions.py")


print("\n", 22)
print("class float([x])")
print(float(25))  # >>> 25.0
print(float("-25"))  # >>> -25.0
# convert an int or number in string to a float number

# Also take strings below:
# sign           ::=  "+" | "-"
# infinity       ::=  "Infinity" | "inf"
# nan            ::=  "nan"
# numeric_value  ::=  floatnumber | infinity | nan
# numeric_string ::=  [sign] numeric_value
float("inf")  # 正无穷大
float("-inf")  # 负无穷大(无穷小)
float("nan")  # not a value


print("\n", 23)
print("format(value[, format_spec])")
# "d" for integer
print(format(123, "d"))  # must be integer
# "f" for float arguments
print(format(123, "f"))  # 总是六位小数
# "b" for binary format
print(format(12, "b"))
# d, f and b are type
# integer
print(format(1234, "*>+7,d"))
# float number
print(format(123.4567, "^-09.3f"))  # 暂时不理解

# 四舍五入与round类似
print(format(1.5, "0.0f"))  # >>> 2
print(format(2.5, "0.0f"))  # >>> 2
print(format(1.55, "0.1f"))  # >>> 1.6
print(format(2.55, "0.1f"))  # >>> 2.5


print("\n", 24)
print("class frozenset([iterable])")
# print(frozenset([1, 2, 3]))
print("see in ZStandardLibrary/learn_set_operation.py")


print("\n", 25)
print("getattr(object, name[, default])")
print("see in ZSimpleLearnings/py_getattr.py")


print("\n", 26)
print("globals()")
print(globals())
# returns the dict of the current module


print("\n", 27)
print("hasattr(object, name)")
# 参数是一个对象和一个字符串。如果字符串是对象的一个属性，则返回True，否则返回False。
# 它的实现是通过调用getattr(object, name)并查看它是否引发一个AttributeError
# 常用于运行函数前做一个boolean判断,如果True即运行函数,False则不运行

lst = [1,2,3]
print(hasattr(lst, "append"))  # >>> True
print(hasattr(lst, "insert"))  # >>> True

strin = "abc"
print(hasattr(strin, "isalpha"))  # >>> True
print(hasattr(strin, "ascii_lowercase"))  # >>> False
import string
print(hasattr(string, "ascii_lowercase"))  # >>> True

# 更多用于oop环境
print("\nOOP test")
class Cls():
    attr1 = "attribute 1"

    def __init__(self, attr2):
        self.attr2 = attr2

    def meth1(self):
        attr3 = "attribute 3"
        return "method 1"

    def meth2(self, num):
        return num**2

obj = Cls("attribute 2")

print(obj.attr1)  # >>> attr1
print(obj.attr2)  # >>> at3
# print(obj.attr3)  # AttributeError
# print(obj.meth1.attr3)  # still AttributeError, a method is not an object therefore has no attributes
print(obj.meth1())   # >>> method 1
print(obj.meth2(6))  # >>> 36

print(type(obj.attr1))  # >>> <class "str">
print(type(obj.attr2))  # >>> <class "str">
print(type(obj.meth1))  # >>> <class "method">  # maybe this can tell whether it is a method or not?
print(type(obj.meth2))  # >>> <class "method">

print(hasattr(obj, "attr1"))        # >>> True
print(hasattr(obj, "attr2"))        # >>> True
print(hasattr(obj, "attr3"))        # >>> False
print(hasattr(obj.meth1, "attr3"))  # >>> False
print(hasattr(obj, "meth1"))  # >>> True  # hasattr() does not differenciate attributes and methods
print(hasattr(obj, "meth2"))  # >>> True

print(set(dir(obj)) - set(dir(Cls)))  # >>> {"attr2"}  # only created in __init__() when an instance is made.
# Therefore Cls has no attribute as attr2 but obj has.

# for more information, check my question on STOF
# https://stackoverflow.com/q/48070833/8435726
# This problem can be solved by using callable()
def hasmethod(obj, method_name):
    return hasattr(obj, method_name) and callable(getattr(obj, method_name))

def hasattribute(obj, method_name):
    return hasattr(obj, method_name) and not callable(getattr(obj, method_name))

print(hasmethod(obj, "meth1"))     # >>> True
print(hasmethod(obj, "attr1"))     # >>> False
print(hasattribute(obj, "attr1"))  # >>> True


print("\n", 28)
print("hash(object)")
# Hash values are just integers which are used to ~
# compare dictionary keys during a dictionary lookup quickly.
print(hash(181))
print(hash(181.23))
print(hash("Python"))
vowels = ("a", "e", "i", "o", "u")
print(hash(vowels))


print("\n", 29)
print("help([object])")
# help() returns the doc str
help(abs)
help(list)
# It's recommenced to try it in your interpreter when you need help to ~
# write Python program and use Python modules


print("\n", 30)
print("hex(x)")
# like bin, hex() returns an integer to hexadecimal number
# start with "0x"
print(hex(123456))
print(format(123456, "x"))
# also use format "x" to skip the "0x" prefix, use "X" to upper the letters


print("\n", 31)
print("id(object)")
# id is very similar to hash, an identity of an object
print(id(5))


print("\n", 32)
print("input([prompt])")
# input()
# to have user input with a hint as the argument


print("\n", 33)
print("class int(x)")
print("class int(x, base=10)")
# don't forget that base can be changed from 2-36.
# base为0意味着完全解释为代码字面值
a = "142AB34"
print(int(a, base=16))  # >>> 21146420
b = "10101"
print(int(b, base=2))   # >>> 21

print("\n", 34)
print("isinstance(object, classinfo)")
# 如果object是clsaainfo的一个实例（或者是classinfo的直接、间接或虚拟子类的实例），那么则返回true。
# 如果对象不是给定类型的对象，则函数始终返回false
# 如果classinfo是对象类型的元组（或递归地，其他这样的元组），如果对象是任何类型的实例，则返回true。如果classinfo不是类型或类型组成的元祖和此类元组，则会引发TypeError异常。
# oop环境
print(isinstance(123, int))  # >>> True
print(isinstance("joker", (int, list, str, tuple)))  # >>> True  # 只要是符合元祖中任一个都返回True


print("\n", 35)
print("issubclass(class, classinfo)")
# 如果 class 是classinfo的子类(直接、 间接或 虚拟) 则返回 true 。
# 一个类被认为是它自己的子类。classinfo可以是类对象的元组，这时classinfo中的每个类对象都会被检查。

print("\n", 36)
print("iter(object[, sentinel])")
# 返回一个迭代器对象

print("\n", 37)
print("len(s)")
# return length of a iterable


print("\n", 38)
print("class list([iterable])")
# turn iterable into a list


print("\n", 39)
print("locals()")
# 暂时不理解


print("\n", 40)
print("map(function, iterable, ...)")
print("see in ZSimpleLearnings/py_high_order_functions.py")


print("\n", 41, 43)
print("max(iterable, *[, key, default])")
print("max(arg1, arg2, *args[, key])")
print("min(iterable, *[, key, default])")
print("min(arg1, arg2, *args[, key])")
print("see in ZSimpleLearnings/py_max_min.py")


print("\n", 42)
print("memoryview(obj)")
# Return the object's memory address?
# memoryview: a bytes-like object is required, not "str"
print(memoryview(b"abcde"))  # >>> <memory at 0x7f3271528048>
print(memoryview("abcde".encode("utf-8")))  # >>> <memory at 0x7f3271528048>


print("\n", 44)
print("next(iterator[, default])")
# consume the next item in an iterator
print("see in ZStandardLibrary/learn_itertools.py")


print("\n", 45)
print("class object()")
# oop 环境


print("\n", 46)
print("oct(x)")
# 将整数转换为八进制字符串。结果是一个合法的Python表达式。
print(oct(120))  # >>> 0o170  "o" means 八进制
print(oct(1999)) # >>> 0o3717


print("\n", 47)
print("open(file, mode="r", buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)")
print("see in ZCodeSnippets/write_and_write_back.py")


print("\n", 48)
print("ord(c)")
# 给定一个表示一个Unicode字符的字符串，返回一个表示该字符的Unicode代码点的整数。
print(ord("a"))  # >>> 97
print(ord(" "))  # >>> 32
print(ord("#"))  # >>> 35
# refer ascii table (0-127)
# but also support more than 0-127
print(chr(1223))  # >>> Ӈ
print(ord("Ӈ"))   # >>> 1223
# The valid range for the argument is from 0 through 1,114,111


print("\n", 49)
print("pow(x, y[, z])")
# return x^y
# 如果提供z参数， 返回x^y再除以z的余数
print(pow(2, 3, 7))  # >>> 8 (2^3=8)
print(pow(2, 3, 7))  # >>> 1 (8//7=1, 余1)


print("\n", 50)
print("print(*objects, sep=" ", end='\n', file=sys.stdout, flush=False)")
print("hello world")

print("\n", 51)
print("class property(fget=None, fset=None, fdel=None, doc=None)")
# oop 环境

print("\n", 52)
print("range(stop)")
print("range(start, stop[, step])")
print("well understood")

print("\n", 53)
print("repr(object)")
# 返回某个对象可打印形式的字符串。
# 主要作用是传送出一个可以给eval()运行的字符串
a = [1,2,3]
print(repr(a))  # >>> [1, 2, 3]
print(a)

b = range(5)
print(repr(b))  # >>> range(0, 5)
print(b)

c = "abcd"
print(repr(c))  # >>> "abcd"   difference is that it will show ""
print(c)        # >>> abcd

import datetime
today = datetime.datetime.now()
# Prints readable format for date-time object
print(today)        # >>> 2017-12-21 20:12:24.180042
# prints the official format of date-time object
print(repr(today))  # >>> datetime.datetime(2017, 12, 21, 20, 12, 24, 180042)


print("\n", 54)
print("reversed(seq)")
# 返回一个反向iterator
a = [1,2,3]
print(list(reversed(a)))
print("see in ZSimpleLearnings/py_sort_sorted_reverse.py")


print("\n", 55)
print("round(number[, ndigits])")
# 当一个值刚好在两个边界的中间的时候， round 函数返回离它最近的偶数。
print(round(1.5, 0))  # >>> 2.0
print(round(2.5, 0))  # >>> 2.0
# 也就是说，对1.5或者2.5的舍入运算都会得到2。


print("\n", 56)
print("class set([iterable])")
# create a set object


print("\n", 57)
print("setattr(object, name, value)")
# 它与getattr()相对应。参数是一个对象、一个字符串和一个任意值。
# 字符串可以是一个已存在属性的名字也可以是一个新属性的名字。
# 该函数将值赋值给属性，只要对象允许。
# OOP环境

print("\n", 58)
print("class slice(stop)")
print("class slice(start, stop[, step])")
# 返回一个slice对象，表示由索引range(start, stop, step)指出的集合。start和step参数默认为None
# slice a list (切片)
a = [1,2,3,4]
b = a[0:2]
print(b)  # >>> [1, 2]
# 但是同样的a[0:2] = [8,9] 则不是在用切片, 而是批量修改a[n for n in range(0, 2)]


print("\n", 59)
print("sorted(iterable[, key][, reverse])")
# sort from small to large (num, alpha)
print("see in ZSimpleLearnings/py_sort_sorted_reverse.py")


print("\n", 60)
print("@ staticmethod(function)")
# 返回function的一个静态方法。


print("\n", 61)
print("class str(object="")")
print("class str(object=b'', encoding='utf-8', errors='strict'")
# turn object into a string version


print("\n", 62)
print("sum(iterable[, start])")
# return the sum of an iterable
# 对于某些使用情况，有很好的替代sum()的方法。
# 连接字符串序列的首选快速方法是调用"".join(sequence)。

# Learn from STOF:
# https://stackoverflow.com/q/52007283/8435726

# Actually sum(a, b) is equal to
# for i in a:
#     b += i
# return b

# So that:
a = [1,2,3,4]
print(sum(a)) # >>> 10
print(sum(a, 2)) # >>>12 # equals to 2 + sum(a)

# But default of start is 0, which in an int.
# So if you want to sum up other types of objects, you must change start
# Example: use sum to merge list
a, b = [1], [2]
# print(sum(a, b))
# >>> TypeError: can only concatenate list (not "int") to list
# print(sum([a, b]))
# # >>> TypeError: unsupported operand type(s) for +: "int" and 'list
print(sum([a, b], []))
# >>> [1, 2]
# equals to [] + [1] + [2]


print("\n", 63)
print("super([type[, object-or-type]])")
# 返回一个代理对象，它委托方法给父类或者type的同级类。
# 这对于访问类中被覆盖的继承方法很有用。
# oop环境


print("\n", 64)
print("tuple([iterable])")
# create a tuple from an iterable


print("\n", 65)
print("class type(object)")
print("class type(name, bases, dict)")
# return the type of the object


print("\n", 66)
print("vars([object])")
print("see in ZSimpleLearnings/py_vars.py")


print("\n", 67)
print("zip(*iterables)")
# very use full to link a group of arrays
print("see in ZSimpleLearnings/py_zip.py")


print("\n", 68)
print("__import__(name, globals=None, locals=None, fromlist=(), level=0)")
# 用于import任何文件名
# surpose a file named 05_if1_guess_number.py, we want to import this file
# mymodule = __import__("05_if1_guess_number")
