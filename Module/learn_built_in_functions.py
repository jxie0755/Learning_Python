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
# The valid range for the argument is from 0 through 1,114,111
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
print(format(123.4567, "^-09.3f"))
# 暂时不理解


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
# 


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


print(38)
print('locals()')


print(39)
print('map()')
print('see in ZSimpleLearnings/lambda_map_filter_reduce.py')

print(40, 42)
print('max() and min()')
print('see in ZSimpleLearnings/max_min.py')


print(41)
print('memoryview()')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')


print()
print('')











































