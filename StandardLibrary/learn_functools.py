"""
functool module
https://docs.python.org/3/library/functools.html#module-functools
"""


import functools

print("functools.partial(func, *args, **keywords")
# 返回一个新的partial对象, 该对象在调用时将采用位置参数args和关键字参数关键字调用的func .
# 如果提供多个参数调用,  它们会被追加给 args. 如果提供额外的关键字参数,  它们会扩展和覆盖 keywords.
# 相当于基于原函数创造一个简化版的快函数

# 例如, partial()可用于创建一个类似于int()函数的可调用, 其中base参数默认为两个
a = "125"
print(int(a))  # 原函数为int()
# >>> 125

newfunc = functools.partial(int)  # 新函数为newfunc()
print(newfunc(a))
# >>> 125

# 为什么这么做? partial()用于部分函数应用程序, 其"冻结"函数的参数和/或关键字的某些部分, 从而产生具有简化声明的新对象.
a = "10101"
print(int(a, base=2))  # 若每次调用都需要输入"base=2"太麻烦
print(int(a, base=8))  # 4161

newfunc = functools.partial(int, base=2)  # 新建一个函数,运行int()的部分功能,专注于base=2
print(newfunc(a))

print(newfunc(a, base=8))  # >>> 4161
# 新函数仍然具备int的全部功能,只是修改了默认base值,以做简化!

print("class functools.partialmethod(func, *args, **keywords)")
# 返回一个新的partialmethod描述器, 它的行为类似于partial, 除了它被设计为用作方法定义而不是直接可调用.
# func必须是descriptor或可调用对象(这两个对象都像常规函数一样被处理为描述器)
# 针对oop环境,创造一个方法,而不是函数,来用



print("functools.reduce(function, iterable[, initializer])")
# 将两个参数的函数累加到序列的项中, 从左到右, 以便将序列减少为单个值.
# See in ZSimpleLearnings/py_high_order_functions.py


print("functools.cmp_to_key(func)")
# Transform an old - style comparison function to a key function.Used with tools that accept key functions (such as sorted(), min(), max(), heapq.nlargest(), heapq.nsmallest(), itertools.groupby()).This function is primarily used as a transition tool for programs being converted from Python 2 which supported the use of comparison functions.
# See more in SimpleLearnings/py_customized_sort.pyk


# partial对象
# partial对象是由partial()创建的可调用对象. 它们有三个只读属性:
# partial.func: 一个可调用对象或函数. 对partial对象的调用将使用新的参数和关键字转发到func.
# partial.args: 最左边的位置参数将被提供给提供给partial对象调用的位置参数.
# partial.keywords: 当调用partial对象时将提供的关键字参数.
# partial对象类似于function对象, 因为它们是可调用的, 弱引用的, 并且可以具有属性. 它们有一些重要的区别.
# 对于实例, 不会自动创建__name__和__doc__属性. 此外, 在类中定义的partial对象的行为类似于静态方法, 并且在实例属性查找期间不会转换为绑定的方法.

import functools


def add(a, b):
    return a + b


print(add(4, 2))  # >>> 6

plus3 = functools.partial(add, 3)
print(plus3(9))  # >>> 12
print(plus3.func)  # >>> <function add at 0x7fb3b58c4e18>
print(plus3.args)  # >>> (3,)
print(plus3.keywords)  # >>> {}
