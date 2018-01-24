# collections module
# https://docs.python.org/3/library/collections.html#module-collections

import collections

print()
print('class collections.ChainMap(*maps)')
# 一个 ChainMap组合多个字典或其它映射集创建一个单一且可更新的视图。如果没有指定 maps ，那么将会用一个空字典作为新chain里面的一个mapping
# 基础的mappings被存储在一个列表当中。这个列表是公开的，可以用 maps 属性访问和更新。没有其它的情况。

# 用于将多个map组合到一起 (把map串联到一起)
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}  # 注意这里'b'为重复的key
chain = collections.ChainMap(dict1, dict2)
print(chain)  # >>> ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})

# .maps(属性),输出一个list
print(chain.maps)  # >>> [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]
chainmap = [dict1, dict2]
print(chainmap == chain.maps)  # >>> True
print(dict1 in chain.maps)  # >>> True
print(list(chain))  # >>> a list of keys, sequence random
print(dict(chain))  # >>> {'b': 2, 'c': 4, 'a': 1} flatten to a regular dict, sequence random

# 但是这个chain的优点是可以输出各种key和value,因为chain object不是单纯的一个list
print(chain.items())  # >>> ItemsView(ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(list(chain.keys()))  # >>> ['b', 'a', 'c'] 过滤掉重复的key, sequence random
print(list(chain.values()))  # >>> [2, 1, 4]  注意这里3没有被记入,要遵循先入为主的原则, sequence random

# 访问这个chain object可以取出各key的value
print(chain['b'])  # >>> 2
print(chain.get('b'))  # >>> 2

# 更改mapping
chain['b'] = 99
print(chain.maps)  # >>> [{'a': 1, 'b': 99}, {'b': 3, 'c': 4}] 只更改第一个值
del chain['b']
print(chain.maps)  # >>> [{'a': 1}, {'b': 3, 'c': 4}] 删除了第一个值以后,后面的key开始起作用
print(chain['b'])  # >>> 3
print(chain.maps[0], ',', chain.maps[1]) # >>> {'a': 1} , {'b': 3, 'c': 4}

# 使用new_child (方法) 添加新dict
dict3 = {'f': 5}
new_chain = chain.new_child(dict3)
print(new_chain.maps)  # >>> [{'f': 5}, {'a': 1}, {'b': 3, 'c': 4}]  # new_child加在前方

# parents(属性)返回一个新的ChainMap，它包含当前实例的除第一个map的所有maps。这个可以用于在搜索中跳过第一个map。
print(new_chain.parents.maps)



print()
print('class collections.Counter([iterable-or-mapping])')

# 计数器工具提供方面、快速的计数方法。
cnt = collections.Counter()  # create empty counter
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
# 很方便的独立给各item统计数目
print(cnt)  # >>> Counter({'blue': 3, 'red': 2, 'green': 1})

# 使用于各种iterable
# 用于统计一个string
c1 = collections.Counter('gallahad')
print(c1)  # >>> Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})
print(c1.most_common(1))  # >>> [('a', 3)]

# 用于统计一个list/tuple
c2 = collections.Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(c2)  # >>> Counter({'blue': 3, 'red': 2, 'green': 1})
print(c2.most_common(1))  # >>> [('blue', 3)]

# 用于统计一个mapping(也就是dict)
c3 = collections.Counter({'red': 4, 'blue': 2})
print(c3)  # >>> Counter({'red': 4, 'blue': 2})
print(c3.most_common(1))  # >>> [('red', 4)]

# 用于统计keyword
c4 = collections.Counter(cats=4, dogs=8)
print(c4)  # >>> Counter({'dogs': 8, 'cats': 4})
print(c4.most_common(1))  # >>> [('dogs', 8)]
print(c4['dogs'])  # >>> 8
print(c4['tigers'])  # >>> 返回0,而不是引发error

# 将计数为0不会删除元素,除非使用del命令
c4['dogs'] = 0
print(c3)  # >>> Counter({'cats': 4, 'dogs': 0})
del c4['dogs']
print(c4)  # >>> Counter({'cats': 4})

# Counter()可以使用的方法
# most common 统计top(x), x=2 below, 输出为一个list
print(cnt) # >>> Counter({'blue': 3, 'red': 2, 'green': 1})
print(cnt.most_common(2))  # >>>  [('blue', 3), ('red', 2)]

# elements()
print(cnt.elements())  # 生成一个迭代器, 对元素重复迭代其计数次。(元素不再以随机顺序返回,而是按照原数据出现顺序。(以前版本可能是))
print(list(cnt.elements()))  # >>> ['red', 'red', 'blue', 'blue', 'blue', 'green']

# subtract([iterable-or-mapping])方法
# 从一个可迭代对象或从另一个映射（或计数器）中减去元素。类似dict.update()，但减去计数，而不是替换它们。
# 输入和输出都可以为零或负。
c = collections.Counter(a=4, b=2, c=0, d=-2)
d = collections.Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)   # >>> Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
print(+c)  # >>> Counter({'a': 3})  remove 0 and negative values

# 同理可以update,也就是增加
c = collections.Counter(a=4, b=2, c=0, d=-2)
d = collections.Counter(a=1, b=2, c=3, d=4)
c.update(d)
print(c)  # >>> Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2})

# 其他attributes
print(c.values())  # >>> dict_values([5, 4, 3, 2])
print(list(c))  # >>> ['a', 'b', 'c', 'd']
print(set(c))  # >>> {'a', 'd', 'c', 'b'}
print(dict(c))  # >>> {'a': 5, 'b': 4, 'c': 3, 'd': 2} convert to a regular dict
print(c.items())  # >>> dict_items([('a', 5), ('b', 4), ('c', 3), ('d', 2)]), convert to a list of (elem, cnt) pairs

#  Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
aa = [('a', 10), ('b', 20), ('c', 30)]
print(dict(aa))  # >>> {'a': 10, 'b': 20, 'c': 30}
ccc = collections.Counter(dict(aa))

n = 2  # n least common elements:
print(c.most_common()[:-n-1:-1])
c.clear() # >>> clear counts, c becomes empty counter

# math way operation
c = collections.Counter(a=3, b=1)
d = collections.Counter(a=1, b=2)
print(c + d)  # >>> Counter({'a': 4, 'b': 3})   # add two counters together:  c[x] + d[x]
print(c - d)  # >>> Counter({'a': 2})           # subtract (keeping only positive counts)
print(c & d)  # >>> Counter({'a': 1, 'b': 1})   # intersection:  min(c[x], d[x])
print(c | d)  # >>> Counter({'a': 3, 'b': 2})   # union:  max(c[x], d[x])

c = collections.Counter(a=2, b=-4)
print(+c)  # >>> Counter({'a': 2})
print(-c)  # >>> Counter({'b': 4})



print()
print('class collections.deque([iterable[, maxlen]])')

# 返回一个由迭代器从左到右(使用append())初始化的双向队列.若未指定初始化的迭代器，返回的双向队列的长度为0
# 双向队列（Deque）是栈和队列的一般化（deque发音和‘deck’一样，是‘double-ended queue’的缩写）。
# Deque是线程安全的。在队列两端添加（append）或弹出（pop）元素的复杂度大约是O(1),所以Deque的效率是很高的。
# 尽管list 对象支持类似的操作, 但是list是专门为固定长度的操作进行了优化，导致了改变列表长度和数据位置的操作
# 例如 pop(0)和 insert(0, v) 操作的复杂度高达O(n)
# 如果 maxlen 未指定或为 None，deque可能长到任意长度。否则，deque的最大长度为指定的maxlen。
# 一旦有界的双向队列满了以后，当有新的元素添加到队列中，就会有相应数量的元素在另一端被丢弃。有界双向队列提供了类似于Unix中tail过滤器的功能。

# Create a deque
lst = [1,2,3,3,4,5]
dec = collections.deque(lst)  # iterable
dec2 = collections.deque(range(5))  # iterator
dec3 = collections.deque('stringdeck')  # string
def f(x):
    for i in range(x):
        yield i**2
print(type(f(5)))
dec4 = collections.deque(f(5))  # generator

print(dec)  # >>> deque([1, 2, 3, 3, 4, 5])
print(dec2)  # >>> deque([0, 1, 2, 3, 4])
print(dec3)  # >>> deque(['s', 't', 'r', 'i', 'n', 'g', 'd', 'e', 'c', 'k'])
print(dec4)  # deque([0, 1, 4, 9, 16])

ddec = collections.deque(lst, 3)  # limit maxlen
print('maxlen is', ddec.maxlen)  # >>> 3
print(ddec)  # >>> deque([3, 4, 5], maxlen=3)  # 注意,这里maxlen的限制是从list的最后items开始,而不是最前

# simple methods to operator deque object (mostly similar to list methods)
dec.append('after')
dec.appendleft('before')
print(dec)  # >>> deque(['before', 1, 2, 3, 4, 5, 'after'])
decc = dec.copy()  # >>> normal copy
#  deccc = dec[:] not slicable, so need to use copy()
print(dec.count(3))  # >>> count number
dec.extend([7,8,9])
print(dec)  # >>> deque(['before', 1, 2, 3, 3, 4, 5, 'after', 7, 8, 9])
dec.extendleft(['x', 'y', 'z'])  # 注意顺序!!!extend left连iterable的顺序也会反转添加
print(dec)  # deque(['z', 'y', 'x', 'before', 1, 2, 3, 3, 4, 5, 'after', 7, 8, 9])
print(dec.index(2))  # >>> 5, return the index of 2 in thie dec
print(dec.insert(5, 'ins'))
print(dec)  # >>> deque(['z', 'y', 'x', 'before', 1, 'ins', 2, 3, 3, 4, 5, 'after', 7, 8, 9])
dec.pop()
dec.popleft()
print(dec)  # >>> deque(['y', 'x', 'before', 1, 'ins', 2, 3, 3, 4, 5, 'after', 7, 8])
dec.remove(3)
print(dec)  # >>> deque(['y', 'x', 'before', 1, 'ins', 2, 3, 4, 5, 'after', 7, 8])  # first time occurence
dec.reverse()
print(dec)  # >>> deque([8, 7, 'after', 5, 4, 3, 2, 'ins', 1, 'before', 'x', 'y'])
dec.rotate(3)  # move n elements from end to head
print(dec)  # >>> deque(['before', 'x', 'y', 8, 7, 'after', 5, 4, 3, 2, 'ins', 1])
dec.rotate(-3)  # rotate the reverse way
print(dec)  # >>> deque([8, 7, 'after', 5, 4, 3, 2, 'ins', 1, 'before', 'x', 'y'])
# dec.clear() # >>> deque([])  # empty the deque

# deque can be transferred to a regular list
print(dec)  # >>> deque([8, 7, 'after', 5, 4, 3, 2, 'ins', 1, 'before', 'x', 'y'])
print(list(dec))  # >>> [8, 7, 'after', 5, 4, 3, 2, 'ins', 1, 'before', 'x', 'y']

# merge two deque?
d1 = collections.deque([1,2,3])
d2 = collections.deque([4,5,6])
d3 = d1 + d2
print(d3)  # >>> deque([1, 2, 3, 4, 5, 6])

# two deque made into a dictionary
print(dict(zip(d1, d2)))  # >>> {1: 4, 2: 5, 3: 6}


print()
print('deque application')
# deque application scenarios
def tail(filename, n):
    """
    Return the last n lines of a file
    :param filename: txt file name as a string
    :param n: last n lines
    :return: a list of last n lines in the txt file
    """
    with open(filename) as f:
        return collections.deque(f, n)
# print(tail('dequetest.txt', n=5))

import itertools
def moving_average(iterable, n=3):
    # calculate 3 consecutve numbers' avaerage value
    it = iter(iterable)  # 目的就是创造一个迭代器使得不会重复迭代
    d = collections.deque(itertools.islice(it, n-1))  # 针对iterator不能使用普通slice method
    d.appendleft(0) # 补位一个0在最左侧
    s = sum((d))
    for elem in it:  # 这里迭代的目的就是新加一个elem,然后从左侧踢出一个elem,维持总数是3个,然后计算average
        s += elem - d.popleft()
        d.append(elem)
        yield s / n
print(list(moving_average([40, 30, 50, 46, 39, 44])))
# >>> [40.0 42.0 45.0 43.0]

# 理解:"一旦有界的双向队列满了以后，当有新的元素添加到队列中，就会有相应数量的元素在另一端被丢弃。"
dec = collections.deque([1,2,3,4,5,6,7,8,9], 5)
print(dec)  # >>> deque([5, 6, 7, 8, 9], maxlen=5)
dec.append('x')
print(dec)  # >>> deque([6, 7, 8, 9, 'x'], maxlen=5)  # kick out 5 from the left
dec.appendleft('y')
print(dec)  # >>> deque(['y', 6, 7, 8, 9], maxlen=5)  # kick out 'x' from the right

# 重写 moving_average()函数
def moving_average_deq(iterable, n=3):
    # calculate 3 consecutve numbers' avaerage value
    it = iter(iterable)  # 目的就是创造一个迭代器使得不会重复迭代
    d = collections.deque(itertools.islice(it, n-1), 3)  # 加入iterator前三项,但是限制deque的maxlen为3
    d.appendleft(0)  # 仍然需要补位一个0
    print('d is now', d)
    for elem in it:  # 同样是维持总数是3个,但是这里依靠deque固定长度的特性
        d.append(elem)
        s = sum(d)
        yield s / n
print(list(moving_average_deq([40, 30, 50, 46, 39, 44])))

def delete_nth(d, n):
    """
    利用rotate来实现deque的slice和删除方法
    :param d: collections object deque
    :param n: nth element to remove
    :return: a slice
    """
    print(d)
    d.rotate(-n)
    print(d)
    d.popleft()
    d.rotate(n)
sample = collections.deque([1,2,3,4,5,6,7])
print(sample)           # >>> deque([1, 2, 3, 4, 5, 6, 7])
delete_nth(sample, 3)       # deque([4, 5, 6, 7, 1, 2, 3]) after rotate(-3)
                            # deque([5, 6, 7, 1, 2, 3])  after popleft()
                            # deque([1, 2, 3, 5, 6, 7]) after rotate(3)



print()
print('class collections.defaultdict([default_factory[, ...]])')

# 返回一个新的类似字典的对象。defaultdict是内置dict类的子类。
# 它覆盖一个方法，并添加一个可写的实例变量。
# 其余的功能与dict类相同，这里就不再记录。
# 第一个参数提供default_factory属性的初始值；它默认为None。所有剩余的参数都视为与传递给dict构造函数的参数相同，包括关键字参数。

# create a defaultdict
lst = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
dic = dict(lst); print(dic)  # >>> {'yellow': 3, 'blue': 4, 'red': 1}

# default_factory表示的是value的类型
# 当每个键第一次遇到时，它不在映射中；因此default_factory函数自动创建一个条目,例如list(),int()。
ddic = ddic = collections.defaultdict()  # 缺省的话 defaultdict(None, {})
ddic = collections.defaultdict(list)  # 使用list作为default factory
print(ddic)  # >>> defaultdict(<class 'list'>, {})

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d)  # >>> defaultdict(<class 'list'>, {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})
print(sorted(d.items()))  # >>> [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
print(dict(d))  # >>> {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
d.update(black=[1,2,3,4])
print(dict(d))  # >>> {'yellow': [1, 3], 'blue': [2, 4], 'red': [1], 'black': [1, 2, 3, 4]}

# 将default_factory设置为set可使defaultdict有助于构建集合字典,规避重复value
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = collections.defaultdict(set)
for k, v in s:
    d[k].add(v)
print(d.items())  # dict_items([('red', {1, 3}), ('blue', {2, 4})])

s = 'mississippi'
# 当一个字母第一次遇到时，映射中缺少该字母，因此default_factory函数调用int()以提供默认计数零。增量操作然后建立每个字母的计数。
d = collections.defaultdict(int)
for k in s:
    d[k] += 1
print(d.items())  # >>> dict_items([('m', 1), ('i', 4), ('s', 4), ('p', 2)])
# 这种用法类似collections.Counter()
d.update(m=10)  # 利用update来改变value (修改)
d.update(x=99)  # (增加)
print(d.items())  # >>> dict_items([('m', 10), ('i', 4), ('s', 4), ('p', 2), ('x', 99)])

d = collections.defaultdict()
print(d)  # >>> defaultdict(None, {})
d.update(name='John', action='ran')
print(d)  # >>> defaultdict(None, {'name': 'John', 'action': 'ran'})

# normal dict operation
print(d.items())   # >>> dict_items([('name', 'John'), ('action', 'ran')])
print(d.keys())    # >>> dict_items([('name', 'John'), ('action', 'ran')])
print(d.values())  # >>> dict_values(['John', 'ran'])
d['name'] = 'Denis'
print(d)  # >>> defaultdict(None, {'name': 'Denis', 'action': 'ran'})
del d['name']
print(d)  # >>> defaultdict(None, {'action': 'ran'})



print()
print('collections.namedtuple(typename, field_names, verbose=False, rename=False)')
# 返回一个叫做 typename 的tuple子类(译注:其实这是一个生成类的工厂方法).
# 这个新的子类用来创建类tuple(tuple-like)的对象,这个对象拥有可以通过属性访问的字段，并且可以通过下标索引和迭代。
# 这个子类的实例还拥有十分友好的文档[docstring(包括类型名和字段名)，
# 可通过__doc__访问]和十分好用的__repr__() 方法，__repr__()以name=value的方式列出了元组中的内容

# 解读field_names:
# field_names 是一个单独的字符串，这个字符串中包含的所有字段用空格或逗号隔开，例如 'x y' 或 'x, y'.
# 另外, field_names 也可以是字符串的列表，例如 ['x', 'y'].
# 除了以下划线开头的名称，任何有效的 Python 标识符都可用于 fieldname 。
# 有效的标识符由字母、 数字和下划线组成，但做不能以数字或下划线开头
# 并且不能是 关键字 例如 class、 for、 return、 global、 pass 或 raise。

# 解读verbose和rename
# 如果 rename参数 为 True, 无效的字段名会被自动转换成位置的名称.
# 例如, ['abc', 'def', 'ghi', 'abc'] 将被转换为 ['abc', '_1', 'ghi', '_3'], 来消除关键字 def 和重复的字段名 abc.
# 如果verbose 为 True, 在类被建立后将打印类的定义.这个选项是过时的; 相反，它打印的是类的 _source 属性(译注:也就是打印源代码).
# namedtuple 的实例中并没有字典, 所以namedtuple并不会比常规的tuple消耗更多的内存，它是轻量级的.

# Basic example
# create a class of namedtuples
Point = collections.namedtuple('Point', ['x', 'y'])
print(Point)  # >>> <class '__main__.Point'>

# create from a dict
coordict = {'x': 101, 'y': 102}  # 注意这里key必须match class arguments
print(Point(**coordict))  # >>> Point(x=101, y=102)


# verbose和rename实例
V = collections.namedtuple('Verb', ['x', 'y'], verbose=False)  # 若verbose=True,则创造V的时候回打印源码, 大部分时候是不必要的
R = collections.namedtuple('Renam', 'large, small, for, class, return', rename=True)
print(R(1,2,3,4,5))  # >>> Renam(large=1, small=2, _2=3, _3=4, _4=5)  # 将python关键字过滤改名为'_index'形式

p = Point(11, 22)  # p is an actuall namedtuple object
# 为一个tuple的各项安排了名字, 这里为坐标
print(p)  # >>> Point(x=11, y=22)
print(tuple(p))  # >>> (11, 22)
print('p[0]', p[0])  # >>> 11
print('p[1]', p[1])  # >>> 22
print(p[0] + p[1])   # >>> 33
# access by name
print(p.x, ',', p.y)  # >>> 11 , 22
# can be unpacked
x, y = p
print(x, y)  # >>> 11 , 22

# 三个method
t = [10, 20]
coor = Point._make(t)  # # ._make(iterable)  create a new example of namedtuple
print(coor)  # >>> Point(x=10, y=20)

OD = coor._asdict()  # return an OrderedDict, key to value mapping
print(OD)  # >>> OrderedDict([('x', 10), ('y', 20)])
print(dict(OD))  # >>> {'x': 10, 'y': 20}  # to normal dict

print(coor)  # >>> Point(x=10, y=20)
print(coor._replace(x=99))  # >>> Point(x=99, y=20)  # create a new namedtuple with new value
print(coor)  # does not change the original value!!!!

# 两个attribute
# print(coor._source)  # return a string that contains python codes for this class, to create a record (打印class源码)
print(coor._fields)  # >>> ('x', 'y')  # a tuple
Color = collections.namedtuple('Color', 'red green blue')  # 参见field_names要求
Pixel = collections.namedtuple('Pixel', coor._fields + Color._fields)  # 即使一个是string一个是tuple也可以相加整合
pp = Pixel(11, 22, 128, 255, 0)
print(pp)  # 用于从已有namedtuple创建新的namedtuple

# 通过getattr(object, attribute)来检索value
print(getattr(pp, 'red'))  # >>> 128

# 通过__doc__字段直接分配自定义文档字符串
Book = collections.namedtuple('DenisBook', 'id, title, authors')
Book.__doc__ += ': Hardcover book'
Book.id.__doc__ = '13-digit ISBN'
Book.title.__doc__ = 'Title of first printing'
Book.authors.__doc__ = 'List of authors sorted by last name'
# print(help(Book))  # this is to help build up the doc string of this class, to keep as a record



print()
print('class collections.OrderedDict([items])')

# 返回一个dict子类的实例，支持通常的dict方法。
# OrderedDict是记住键首次插入顺序的字典。
# 如果新条目覆盖现有条目，则原始插入位置保持不变。
# 删除条目并重新插入会将其移动到末尾。

# regular dict is order in python 3.6, but:
# 1. it's not in the spec
# 2. you shouldn't rely on it
# 3. python can't figure out if you're relying on it, so no error will be raised
# 4. subtle bugs are sure to be introduced by people who "know" this "feature" exists and use it.

# basic example
lst = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
odic = collections.OrderedDict(lst)
print(odic)           # >>> OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print(odic.items())   # >>> odict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print(odic.keys())    # >>> odict_keys(['a', 'b', 'c', 'd'])
print(odic.values())  # >>> odict_values([1, 2, 3, 4])

# basic operation
print(odic['c'])  # >>> 3
odic['e'] = 5
print(odic)  # >>>OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

# 除了通常的映射方法之外，有序字典还支持使用reversed()的反向迭代。
print(list(reversed(odic)))  # >>> ['e', 'd', 'c', 'b', 'a']
rdiclist = [(k, v) for k, v in reversed(odic.items())]
print(rdiclist)  # >>> [('e', 5), ('d', 4), ('c', 3), ('b', 2), ('a', 1)]

# keep dict ordered, by both regular and ordered dict
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}  # regular dictionary

regdic1 = dict(sorted(d.items()))  # key=lambda x:x[0] 可省略
print(regdic1)  # >>> {'apple': 4, 'banana': 3, 'orange': 2, 'pear': 1}
regdic2 = dict(sorted(d.items(), key=lambda x:x[1]))
print(regdic2)  # >>> {'pear': 1, 'orange': 2, 'banana': 3, 'apple': 4}
regdic3 = dict(sorted(d.items(), key=lambda x:len(x[0])))  # sort by length of key
print(regdic3)  # >>> {'pear': 1, 'apple': 4, 'banana': 3, 'orange': 2}

orddic1 = collections.OrderedDict(sorted(d.items()))  # key=lambda x:x[0] 可以省略
print(orddic1)    # >>> OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
orddic2 = collections.OrderedDict(sorted(d.items(), key=lambda x:x[1]))
print(orddic2)    # >>> OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])
orddic3 = collections.OrderedDict(sorted(d.items(), key=lambda x:len(x[0])))
print(orddic3)    # >>> OrderedDict([('pear', 1), ('apple', 4), ('banana', 3), ('orange', 2)])

# delete key pair will keep the order
del regdic2['orange']
print(regdic2)  # >>> {'pear': 1, 'banana': 3, 'apple': 4}
del orddic2['orange']
print(orddic2)  # >>> OrderedDict([('pear', 1), ('banana', 3), ('apple', 4)])



print()
print('class collections.UserDict([initialdata])')

# UserDict是一个包裹了字典的对象。对这个类的需要已经部分地被直接从dict子类化的能力所代替；
# 但是，此类可以更容易使用，因为底层字典可作为属性访问。
# UserDict仿照字典。实例的内容保存在一个普通的字典当中，可以通过UserDict实例的属性data访问。
# 如果提供initialdata, data就会被初始化为initialldata

# 一般来说没什么用
# 主要使用来拷贝一个字典的数据，而不是共享同一份数据。

lst = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
udic = collections.UserDict(lst)
print(udic)  # >>> {'a': 1, 'b': 2, 'c': 3, 'd': 4}  # looks no different than regular dict
print(udic.data)  # >>> {'a': 1, 'b': 2, 'c': 3, 'd': 4}  # 输出一个regular dict

regdic = dict(lst)
udic2 = collections.UserDict(regdic)  # initialdata 可以是paried list也可以是一个dict
print(udic2)  # >>> {'a': 1, 'b': 2, 'c': 3, 'd': 4}

emptudic = collections.UserDict()
print(emptudic)  # >>> {} 可为空
emptudic['test'] = 1234
print(emptudic)  # >>> {'test': 1234} # no difference from regular dict



print()
print('class collections.UserList([list])')

# 这个类充当列表对象的包装器。
# 它是一个有用的基类，你自己的类列表类可以从它们继承，覆盖现有的方法或添加新的。这样，可以向列表中添加新的行为。
# 这个类的需要已经部分地被直接从list子类化的能力所取代；
# 但是，此类可以更容易使用，因为底层列表可作为属性访问。

lst = [1,2,3,4]
ulst = collections.UserList(lst)
print(ulst)  # >>> [1, 2, 3, 4]
print(type(ulst.data))  # regular list



print()
print('class collections.UserString([sequence])')

# 类UserString充当字符串对象的包装器。这个类的需要已经部分地被从str直接子类化的能力所取代；
# 但是，此类可以更容易使用，因为底层字符串可作为属性访问。

stri = 'abcdefg'
ustri = collections.UserString(stri)
print(ustri)  # >>> abcdefg
print(type(ustri.data))  # >>> regular string
