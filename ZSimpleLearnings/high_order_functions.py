

# filter(function, sequence)：对sequence中的item依次执行function(item)，将执行结果为True的item组成一个List/String/Tuple（取决于sequence的类型）返回

# 定义一个函数,鉴别一个数不能被2整除的数.
def f(x): return x % 2 != 0
print(list(filter(f, range(0, 10))))
# >>> [1, 3, 5, 7, 9]

from itertools import filterfalse
print(list(filterfalse(f, range(0, 10))))
# >>> [0, 2, 4, 6, 8]
# See itertools.filterfalse() for the complementary function that returns elements of iterable for which function returns false.

def f(x): return x
print(list(filter(f, ['Denis', '' 'Xie'])))
# >>> ['Denis', 'Xie']

# map(function, sequence) ：对sequence中的item依次执行function(item)，将执行结果组成一个List

# 与上面那个例子相同的函数,鉴别能否被2整除
def f(x): return x % 2 != 0
print(list(map(f, range(0, 10))))
# >>> [False, True, False, True, False, True, False, True, False, True]

# map也支持多个sequence，这就要求function也支持相应数量的参数输入：

def add(x, y): return x+y
print(list(map(add, range(8), range(8))))  # 如果两个sequence长度不同,只执行相同的部分,多余部分被忽略
# >>> [0, 2, 4, 6, 8, 10, 12, 14]
print(list(map(add, 'Denis', 'Cindy')))  # string也是sequence!!
# >>> ['DC', 'ei', 'nn', 'id', 'sy']

# does not do what filter can do.
# unless filter a lambda x: x.
def g(x):
    if x % 2 != 0:
        return x
print(list(map(g, range(0,10))))
# >>> [None, 1, None, 3, None, 5, None, 7, None, 9]


# Testing multiple map()
l = [1, -1, '2', '0', 33, '-5', 9]
print(max(list(map(abs, list(map(int, l))))))
# >>> 33

# reduce(function, sequence, starting_value)：对sequence中的item顺序迭代调用function, 函数必须要有2个参数。要是有第3个参数，则表示初始值，可以继续调用初始值，返回一个值。

# reduce()函数即为化简函数，它的执行过程为：每一次迭代，都将上一次的迭代结果（注：第一次为init元素，如果没有指定init则为seq的第一个元素）与下一个元素一同传入二元func函数中去执行。

from functools import reduce

def add(x,y): return x + y
print(reduce(add, range(1, 11)))      # >>> 55
# （注：1+2+3+4+5+6+7+8+9+10 = 55）

print(reduce(add, range(1, 11), 20))  # >>> 75
# （注：20+1+2+3+4+5+6+7+8+9+10 = 75）

l = [2, 3, 4]
print(reduce(pow, l))  # >>> 4096
# equal to (2**3)**4, 注意括号

# lambda：这是Python支持一种有趣的语法，它允许你快速定义单行的最小函数，类似与C语言中的宏，这些叫做lambda的函数，是从LISP借用来的，可以用在任何需要函数的地方：
g = lambda x: x * 2
print(g(3))  # >>> 6

# Testing lambda
# create anonymous function (with no name)
# lambda是制造一个匿名函数,只运行一次,省时省力

# in regular way:
def sq(x):
    return x**x
map(sq, [y for y in range(10)])
# this created a function called sq()

# in lamda way:
map(lambda x: x**x, [y for y in range(10)])

# define a function that x is the argument
# write out the function: x**x
# the parameter is to acutally be used as the argument

# example:
l = [1, -1, '2', '0', 33, '-5', 9]
print(list(map(lambda x: x ** 2, list(map(int, l)))))
# >>> [1, 1, 4, 0, 1089, 25, 81]

# avoid using reduce()
from functools import reduce
l = [2, 3, 4, 5]

print(reduce(pow, l))      # >>> 1152921504606846976

result = l[0]
for i in range(1, (len(l))):
    result **= l[i]
print(result)              # >>> 1152921504606846976


# 小问题：去除列表mylist中的空字符
mylist=['A','B','','C',None,'D']
# 暴力解决：
for item in mylist:
    if item=="" or item==None:
        del item
# 优秀解决：filter+lambda
newlist = list(filter(lambda x: x, mylist))
