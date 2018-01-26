# itertool module
# https://docs.python.org/3/library/itertools.html#module-itertools


print()
print('next()')
# 一个很有用的funtion,用于获取iterable中的下一个item.
# 可以被广泛配合用于itertools
a=[1,2,3]
# print(next(a)) 注意这样不能使用,必须是iterator.而不是iterable
# next() 可以追加一个deault value,如果遍历完所有next(), 不添加default则出现错误StopIteration,或者添加default则可以固定返回一个default值

# iter()
# 把一个iterable变成iterator
iter_a = iter(a)
print(next(iter_a))
# 这个时候,就可以使用很多针对iterator的命令,比如之前的next()

import itertools
print()
print('itertools.count()')
# 不停的往后计数, 可以选择计数间隔
result = []
for i in itertools.count(10):
    result.append(i)
    if i >= 20:
        break
print(result)  # >>> [10, 11, 12, 13, 14, 15]

result = []
for i in itertools.count(10, 2):
    result.append(i)
    if i >= 20:
        break
print(result)  # >>> [10, 12, 14, 16, 18, 20]


print()
print('itertools.cycle()')
# 不停的循环一个iterable中的每一个element,可以是string也可以是list
g = itertools.cycle('ABCD')
print(next(g))  # >>> A
print(next(g))  # >>> B
print(next(g))  # >>> C
print(next(g))  # >>> D
print(next(g))  # >>> A
xlist = ["square", "triangle", "circle", "pentagon", "star", "octagon"]
g = itertools.cycle(xlist)
for i in range(8):
    sample = next(g)   # next()正确用法,g为生成的iterator
    print('Drawing:', sample)
# >>>
# Drawing: triangle
# Drawing: circle
# Drawing: pentagon
# Drawing: star
# Drawing: octagon
# Drawing: square
# Drawing: triangle
# Drawing: circle


print()
print('itertools.repeat()')
print(list(itertools.repeat(10, 3)))  # >>> [10, 10, 10]


print()
print('itertools.accumulate(iterable[, func])')
# 创建的迭代对象返回被计算的sums值或者其它二元函数的结果(通过指定func参数)。func应该是接收两个参数的函数。输入iterable的元素可以是可以作为func的参数接受的任何类型。
# 如果输入iterable为空，则输出iterable也将为空。

import functools

aa = [1,2,3,4]
print(list(itertools.accumulate(aa)))
# >>> [1, 3, 6, 10]
# 对比reduce函数
def add(x,y):
    return x + y
print(functools.reduce(add, aa))
# >>> 10 (计算1+2+3+4 = ?)
# 可以指定func,不一定是计算sum
def mult(x,y):
    return x * y
print(functools.reduce(add, aa))
aa = [1,2,3,4]
print(list(itertools.accumulate(aa, func=mult)))
# >>> [1, 2, 6, 24]
# 对比reduce函数
print(functools.reduce(mult, aa))
# >>> 24
# 可以看出,reduce只计算了accumlate的最后一项,accumulate范围更大.


print()
print('itertools.chain(*iterables)')
# 创建一个迭代器，从第一个迭代器返回元素，直到它耗尽，然后继续下一个迭代器，直到所有的迭代器都用尽。
# To merge all the items in lists of a list
list2d = [[1,2,3],['a','b','c'], [7], [8,9]]
print(list(itertools.chain(*list2d)))
# >>> [1, 2, 3, 'a', 'b', 'c', 7, 8, 9]

aa = [1,2,3]
bb = ['a', 'b', 'c']
print(list(itertools.chain(aa, bb)))  # >>> [1, 2, 3, 'a', 'b', 'c']


print()
print('classmethod chain.from_iterable(iterable)')
# chain()的替代构造函数。从一个可计算延迟的可迭代参数获取链接的输入。
print(list(itertools.chain.from_iterable(list2d)))  # only take one argument
# >>> [1, 2, 3, 'a', 'b', 'c', 7, 8, 9]


# 生成循环iterator
def generate_iterables():
    for i in range(4):
        yield range(i+2)  # 注意这里+2,是为了抵消range末数不计入

result = []
for i in itertools.chain.from_iterable(generate_iterables()):
    result.append(i)
print(result)  # >>> [0, 1, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4]

# 生成无限循环iterator
def generate_iterables2():
    while True:
        for i in range(4):
            yield range(i+2)
result = []
for i in itertools.chain.from_iterable(generate_iterables2()):
    result.append(i)
    if len(result) >= 30:
        break
print(result)  # >>> [0, 1, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4,
                    # 0, 1, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4, 0, 1]
# 区别
# chain() takes 0 or more arguments, each an iterable
# chain.from_iterable() takes one argument which is expected to produce the iterables. but this iterables can be any iterator that yields the iterables.
# The key advantage of from_iterables lies in the ability to handle large (potentially infinite) number of iterables since all of them need not be available at the time of the call.


print()
print('itertools.combinations(iterable, r)')
# 从输入可迭代返回r个元素的长度的子序列
# 组合以词典排序顺序发出。因此，如果输入可迭代被排序，则组合元组将以排序顺序产生。
# 元素根据它们的位置而不是它们的值被视为唯一的。因此，如果输入元素是唯一的，则在每个组合中将不存在重复值。
print([str(x) + str(y) for x,y in itertools.combinations('ABCD', 2)])
# >>> [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
print([str(x) + str(y) + str(z) for x,y,z in itertools.combinations(range(4), 3)])
# >>> ['012', '013', '023', '123']
print([str(x) + str(y) for x,y in itertools.combinations('AAAA', 2)])
# >>> ['AA', 'AA', 'AA', 'AA', 'AA', 'AA']  注意这里虽然string是'AAAA'.但是不同的A被视为不同元素,不会形成只有一个'AA'的情况
# 相当于排列组合中的组合,不讲究顺序,但是选出所有的组合


print()
print('itertools.combinations_with_replacement(iterable, r)')
# 从输入可迭代返回元素的r长度子序列，允许单个元素重复一次以上。
# 组合以词典排序顺序发出。因此，如果输入可迭代被排序，则组合元组将以排序顺序产生。
# 元素根据它们的位置而不是它们的值被视为唯一的。因此，如果输入元素是唯一的，则生成的组合也将是唯一的。
print([str(x) + str(y) for x,y in itertools.combinations_with_replacement('ABC', 2)])
# >>> ['AA', 'AB', 'AC', 'BB', 'BC', 'CC']
print(sorted(list(set([str(x) + str(y) for x,y in itertools.combinations('ABCABC', 2)]))))
# >>> ['AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC']
print(sorted(list(set([str(x) + str(y) for x,y in itertools.combinations('AABBCC', 2)]))))
# >>>[ 'AA', 'AB', 'AC', 'BB', 'BC', 'CC']
# 注意这里,如果想用combination()实现,则必须使用'AABBCC'而不是'ABCABC'
# 使用set()来清除重复元素,然后再次list(),顺序问题参考Zsimplelearnings/remove_repeating_in_list.py


print()
print('itertools.permutations(iterable, r=None)')
# 返回可迭代中的元素的连续r长度排列。
# 如果r未指定或None，则r默认为可迭代的长度，长度排列。
# 排列按照字典排序顺序排列。因此，如果输入iterable被排序，则排列元组将以排序顺序产生。
# 元素根据它们的位置而不是它们的值被视为唯一的。因此，如果输入元素是唯一的，则在每个排列中将不存在重复值。
print([x+y for x, y in itertools.permutations('ABC', 2)])
# >>> ['AB', 'AC', 'BA', 'BC', 'CA', 'CB']
print([str(x) + str(y) + str(z) for x,y,z in itertools.permutations(range(3))])
# >>> ['012', '021', '102', '120', '201', '210']
# 相当于排列组合中的排列,顺序也讲究


print()
print('itertools.compress(data, selectors)')
# 创建一个迭代器，用于过滤数据中的元素，只返回在选择器中具有对应元素的元素，其计算结果为True。当数据或选择器迭代可用时停止。
data = 'ABCDEF'
selector = [1,0,1,0,1,1,]  # 注意这里0为False,其他1,2,3任何非空都是True
print(list(itertools.compress(data, selector)))
# >>> ['A', 'C', 'E', 'F']
# 相当于利用zip来审核value,然后返回一个key
print(list(d for d, s in zip(data, selector) if s))
# >>> ['A', 'C', 'E', 'F']


print()
print('itertools.dropwhile(predicate, iterable)')
# 创建一个迭代器，只要谓词为真，就从迭代中删除元素；之后，返回每个元素。
# 注意，迭代器不会产生任何输出，直到谓词首次变为假，因此它可能有一个冗长的启动时间。
# 若没有False,则输出空iterable
print(list(itertools.dropwhile(lambda x: x<5, [1,4,6,7,4,1])))
# >>> [6, 7, 4, 1]


print()
print('itertools.takewhile(predicate, iterable)')
# 创建一个迭代器，只要谓词为真，它就返回可迭代的元素。
print(list(itertools.takewhile(lambda x: x<5, [1,4,6,7,4,1])))
# 可以理解为dropwhile()的反函数


print()
print('itertools.filterfalse(predicate, iterable)')
# 创建一个迭代器，过滤可迭代元素，只返回谓词为False的元素。
# 如果谓词是None，则返回false的项目。
print(list((itertools.filterfalse(lambda x: x<5, [1,4,6,7,4,1]))))
# >>> [6, 7]

# 注意dropwhile和filterfalse的区别, 一个是False出现之后的所有item,一个是过滤出所有False的item.
# 注意filter()与之相反,但是不属于itertools范围,而是属于built-in函数


print()
print('itertools.groupby(iterable, key=None)')
# 创建一个迭代器，从可迭代返回连续的键和组。
# 键是计算每个元素的键值的函数。如果未指定或None，则键默认为标识函数，并且不更改元素。
# 通常，迭代需要已经在相同的键函数上排序。
from operator import itemgetter #itemgetter用来去dict中的key，省去了使用lambda函数
from itertools import groupby #itertool还包含有其他很多函数，比如将多个list联合起来。。
d1={'name':'AAA','age':18,'country':'China'}
d2={'name':'BBB','age':19,'country':'USA'}
d3={'name':'CCC','age':20,'country':'JP'}
d4={'name':'DDD','age':21,'country':'USA'}
d5={'name':'EEE','age':22,'country':'USA'}
d6={'name':'FFF','age':23,'country':'China'}
lst=[d1,d2,d3,d4,d5,d6]

#通过country进行分组：
lst.sort(key=itemgetter('country')) #需要先排序，然后才能groupby。lst排序后自身被改变
# 不sort的话,同类型items会散落,形成很多同类的小分组
lstg = groupby(lst,itemgetter('country'))
#lstg = groupby(lst,key=lambda x:x['country']) 等同于使用itemgetter()

for key,group in lstg:
    print(key, group)
# >>>
# China <itertools._grouper object at 0x7f141e7ec240>
# JP <itertools._grouper object at 0x7f141e7ec278>
# USA <itertools._grouper object at 0x7f141e7ec240>
# 可以看出lstg实际上是一个dict,key就是先前制定的key,value是一个iterable
# 注意iterable只能使用一次,所以这里不会再次运行,只是简化代码方便阅读:
for key,value_group in lstg:
    for g in value_group: #value_group是一个迭代器，包含了所有的分组列表
        print(g, 'has a key of', key)
# >>>
# {'name': 'AAA', 'age': 18, 'country': 'China'} has a key of China
# {'name': 'FFF', 'age': 23, 'country': 'China'} has a key of China
# {'name': 'CCC', 'age': 20, 'country': 'JP'} has a key of JP
# {'name': 'BBB', 'age': 19, 'country': 'USA'} has a key of USA
# {'name': 'DDD', 'age': 21, 'country': 'USA'} has a key of USA
# {'name': 'EEE', 'age': 22, 'country': 'USA'} has a key of USA
for k, g in lstg:
    print(list(g))
# >>>
# [{'name': 'AAA', 'age': 18, 'country': 'China'}, {'name': 'FFF', 'age': 23, 'country': 'China'}]
# [{'name': 'CCC', 'age': 20, 'country': 'JP'}]
# [{'name': 'BBB', 'age': 19, 'country': 'USA'}, {'name': 'DDD', 'age': 21, 'country': 'USA'}, {'name': 'EEE', 'age': 22, 'country': 'USA'}
for k, g in lstg:
    print(k, 'count:', len(list(g)))
# >>>
# China count: 2
# JP count: 1
# USA count: 3

for key, value in itertools.groupby(range(12), lambda x: x>6):
    print(key, list(value))
# >>> False [0, 1, 2, 3, 4, 5, 6]
# >>> True [7, 8, 9, 10, 11]

aa = ['a','a','c','d']
for k, v in groupby(aa):
    print(k, list(v))
# >>> a ['a', 'a']
# >>> c ['c']
# >>> d ['d']


print()
print('itertools.islice(iterable, stop)')
print('itertools.islice(iterable, start, stop[, step])')
# 创建一个迭代器，从迭代器返回选定的元素。如果start不为零，则跳过来自可迭代的元素，直到达到开始。
# 之后，连续返回元素，除非步骤设置为高于导致项目被跳过的元素。
# 如果停止是None，则迭代继续，直到迭代器耗尽，如果有的话；否则，它停在指定位置。
# 不像常规切片，islice()不支持开始，停止或步骤的负值。可用于从内部结构已展平的数据中提取相关字段
print(list(itertools.islice('ABCDEFG', 3)))  # means range(0,3) output items at position 0, 1, 2.
# >>> ['A', 'B', 'C']
print(list(itertools.islice('ABCDEFG', 2, 6)))  # means range(2,6), output items at position 2,3,4,5
# >>> ['C', 'D', 'E', 'F']
print(list(itertools.islice('ABCDEFG', 2, None)))  # means range(2, len(iterable)+1), 'None' means to the end
# >>> ['C', 'D', 'E', 'F', 'G']
print(list(itertools.islice('ABCDEFG', 0, None, 2)))  # means range(2, len(iterable)+1), step), to the end
# >>> ['A', 'C', 'E', 'G']
print(list(itertools.islice('ABCDEFG', 2, 2)))  # returns empty list
# >>> []


print()
print('itertools.product(*iterables, repeat=1)')
# 输入迭代的笛卡尔乘积。
# 大致等同于生成器表达式中的嵌套for循环。例如，乘积（A， B）返回与（（x，y） for x in A for y in B）。
a = [1, 2, 3]
b = [4, 5, 6]
print([x*y for x in a for y in b])
# >>> [4, 5, 6, 8, 10, 12, 12, 15, 18]
print(list(itertools.product(a, b)))
# >>> [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
print([x*y for x, y in itertools.product(a, b)])
# >>> [4, 5, 6, 8, 10, 12, 12, 15, 18]
c = 'ABC'
d = 'xy'
print([x + y for x, y in itertools.product(c, d)])
# >>> ['Ax', 'Ay', 'Bx', 'By', 'Cx', 'Cy']
for i in itertools.product((range(2)), repeat=3):
    print(i)
# >>>
# (0, 0, 0)
# (0, 0, 1)
# (0, 1, 0)
# (0, 1, 1)
# (1, 0, 0)
# (1, 0, 1)
# (1, 1, 0)
# (1, 1, 1)
# 同理: itertools.product(c, d, repeat=2)
# equal to itertools.product(c, d, c, d)


print()
print('itertools.starmap(function,iterable)')
# 创建一个迭代器，使用从可迭代获得的参数计算函数。当参数参数已经被分组到来自单个可迭代的元组（数据已经被“预压缩”）时，使用map()
print(list(itertools.starmap(pow, [(2,2), (3,2), (10,3)])))
# >>> [4, 9, 1000]
# equal to
print(list(map(pow, [2,3,10], [2,2,3])))


print()
print('itertools.tee(iterable, n=2)')
# 用于从 iterable 创建 n 个独立的迭代器，以元组的形式返回，n 的默认值是 2。
itertools.tee('abcd')   # n 默认为 2，创建两个独立的迭代器
# (<itertools.tee object at 0x1049957e8>, <itertools.tee object at 0x104995878>)
iter1, iter2, iter3 = itertools.tee('abcde', 3)  #如果是默认,就iter1,iter2 =, 如果是指定n,则必须也配齐n个,不得缺少
print(list(iter1))
# >>> ['a', 'b', 'c', 'd', 'e']
print(list(iter2))
# >>> ['a', 'b', 'c', 'd', 'e']
# print(list(iter3)) # 可以不输出,但是不能少指定


print()
print('itertools.zip_longest(*iterables, fillvalue=None)')
# 创建一个迭代器，聚合来自每个迭代器的元素。如果迭代的长度不均匀，则缺少的值将被填充fillvalue。迭代继续，直到最长可迭代被耗尽
print(dict(itertools.zip_longest('ABCD', 'xy', fillvalue='-')))
# >>> {'A': 'x', 'B': 'y', 'C': '-', 'D': '-'}
# 基本上相当于zip,只不过zip终止于最短iterable,这个终止于最长iterable,通过fillvalue