# A try out for all the built-in functions in python

print(abs(-4))  # >>> 4
# absolute value
# argument: int and float
# return the

print(all([0, 4]))  # >>> False
print(all([]))  # >>> True
# argument: iterable objects
# return True if all elements of the iterable are true
# if the iterable is empty, return True

print(any([0, 4]))  # >>> True
# argument: iterable objects
# return True if any elements of the iterable are true
# if the iterable is empty, return True


print(ascii('ö'))  # >>> xf6n
print('Pyth\xf6n')  # >>>Pythön
# argument: an object
# return a string containing a printable representation of an object, but escape the non-ASCII characters in the string returned by repr() using \x, \u, \U escapes.
# For example, ö is changed to \xf6n, √ is changed to \u221a


print(bin(3))  # >>> 0b11
print(bin(-10))  # >>> -0b1010
print(format(10, 'b'))  # >>> 1010, this can remove the '0b'
# convert to binary number with a prefix '0b'
# argument: an integer number
# return the binary value


print(bool(0))  # >>> False
print(bool('0'))  # >>> True
print(bool(None))  # >>> False
print(bool([]))  # >>> False
# argument can be any object
# return True or False
# None，False，0, 0.0,空字符串'', 空元组(), 空列表[]， 空字典{} 这些算作False
# 其他皆为True


print(bytearray([0, 100, 255]))  # >>> bytearray(b'\x00d\xff')
print(bytearray(12))  # >>> bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
print(bytes([0, 100, 255]))  # >>> b'\x00d\xff'
print(bytes(12))  # >>> b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
# 暂时不理解


print(callable(1))  # >>> False
print(callable(abs))  # >>> True, function is callable
print(callable([1, 2]))  # >>> True, function is callable
print(callable(zip()))  # >>> False, if with '()'
# argument: any object
# return True if it is callable, otherwise False


print(chr(97))  # >>> a, refer the ascii table
print(ord('a'))  # >>> 97, the inverse function of chr
# The valid range for the argument is from 0 through 1,114,111
# return the character accordingly


print(classmethod(abs(5)))
# 将函数包装成类方法
# 暂时不理解


# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
# 暂时不理解


print(complex('1+2j'))
# 返回值形式为real + imag * 1j的复数，或将字符串或数字转换为复数
# does not allow white space in the string ('1 + 2j') will raise error
# 暂时不理解divmod



# delattr(object, 's')
# 这个函数和setattr()有关。参数是一个对象和一个字符串。
# 字符串必须是对象的某个属性的名字。只要对象允许，这个函数删除该名字对应的属性。
# delattr(x, 'foobar')等同于del x.foobar。
# 暂时不理解

print(dict(zip([1, 2, 3], ['a', 'b', 'c'])))
# create a dictionary


print(dir())
# 如果没有参数，返回当前本地作用域内的名字列表。
# 如果有参数，尝试返回参数所指明对象的合法属性的列表。


print(divmod(7, 2))  # >>> (3, 1) return a tuple
for i in divmod(7, 2):
    print(i)
# Take two (non complex) numbers as arguments
# return a pair of numbers consisting of their quotient and remainder


l = ['apple', 'banana', 'pear', 'mango']
print(list(enumerate(l, start=1)))
# >>> [(1, 'apple'), (2, 'banana'), (3, 'pear'), (4, 'mango')]
print(dict(enumerate(l, start=1)))
# >>> {1: 'apple', 2: 'banana', 3: 'pear', 4: 'mango'}
# argument: iterable object, default start with 0.
# return a paired value, but needs a container (list, dict, etc)


# eval(expression, globals=None, locals=None)
# 暂时不理解


# exec(object[, globals[, locals]])
# 暂时不理解

#
print(list(filter(abs, [-1, -2, 3])))
# is equivalent to the generator expression (item for item in iterable if function(item))


print(float(25))  # >>> 25.0
print(float('-25'))  # >>> -25.0
# convert an int or number in string to a float number



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

# print(frozenset([1, 2, 3]))
# 暂时不理解

class Person:
    age = 23
    name = "Adam"

person = Person()
print('The age is:', getattr(person, "age"))
print('The age is:', person.age)


class Person:
    age = 23
    name = "Adam"

person = Person()

# when default value is provided
print('The sex is:', getattr(person, 'sex', 'Male'))
# getattr(object, name[, default]), Male is the default value for sex

print(globals())
# returns the dict of the current module


# help() returns the doc str
help(abs)
help(list)
# It's recommenced to try it in your interpreter when you need help to ~
# write Python program and use Python modules


# like bin, hex() returns an integer to hexadecimal number
# start with '0x'
print(hex(123456))
print(format(123456, 'x'))
# also use format 'x' to skip the '0x' prefix, use 'X' to upper the letters


# Hash values are just integers which are used to ~
# compare dictionary keys during a dictionary lookup quickly.
print(hash(181))
print(hash(181.23))
print(hash('Python'))
vowels = ('a', 'e', 'i', 'o', 'u')
print(hash(vowels))


# input()
# to have user input with a hint as the argument


# id is very similar to hash, an identity of an object
print(id(5))




