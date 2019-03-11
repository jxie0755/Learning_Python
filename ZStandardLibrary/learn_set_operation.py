# set operation
# https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset

print('class set([iterable]))')
print('class frozenset([iterable])')

# Set 包含两个,一个是set,一个是frozenset.

# 集合对象是一个由互不相同的hashable对象组成的无序集合
# 它与tuple或者list非常类似,但是最大区别就是无序且不允许出现重复元素. 常见的使用包括成员测试、从序列中删除重复项和计算数学运算（如交、并、差和对称差）

# 因此,集合支持x in set、len(set)以及for x in set
# 但作为一个无序的集合，集合不记录元素位置和插入顺序. 因此，集合不支持索引、 切片、 或其它类似于序列的行为

# set 类型是可变的 — 可以使用add()和remove()方法来更改内容. 因为它是可变的，所以它没有哈希值(not hashable)且不能用作字典的键或另一个集合的元素。
# frozenset 类型是不可变的，hashable - 其内容创建后不能更改；它因此可以用作字典键或作为另一个集合的元素


# create a set

# use set() to create from a list or a tuple
lst = [1,2,5,3,3,3,4,5]
tup = (1,3,3,5,7,7,9)
tup2 = ('a', 's', 'd', 'f')
print(set(lst))  # >>> {1, 2, 3, 4, 5}
print(set(tup))  # >>> {1, 3, 5, 7, 9}       # numbers sequence not showed random, but stll no sequence
print(set(tup2)) # >>> {'b', 'a', 'd', 'c'}  # string sequence showed random (no sequence)

# from dict, create a set of keys or values.
dic = {'a': 1, 'b': 3, 'c': 3, 'd': 2}
print(set(dic))  # >>> {'a', 'b', 'c'}
print(set(dic.values())) # >>> {1, 2, 3}

# create from using {} directly for NON-EMPTY set
set1 = {4,5,6};   print(set1)  # >>> {4, 5, 6}
set2 = {4,5,5,6}; print(set2)  # >>> {4, 5, 6}  # still filter the repeating

# create empty set
emptset = set([])
print(emptset)  # >>> set()



# create frozenset
# frozenset是冻结的集合，它是不可变的，存在哈希值，好处是它可以作为字典的key，也可以作为其它集合的元素。

# 基本相同,但是不能直接使用{}
print(frozenset(lst))   # >>> frozenset({1, 2, 3, 4, 5})
print(frozenset(tup))   # >>> frozenset({1, 3, 5, 7, 9})
print(frozenset(tup2))  # >>> frozenset({'s', 'd', 'a', 'f'})

# there is no point to create empty frozenset, but you still can
emptfset = frozenset([])
print(emptfset)  # >>> frozenset()

# 一旦创建便不能更改，没有add，remove方法。
a = [0, 1, 1, 1, 2, 3, 3, 4]
fst = frozenset(a)
# fst.add(9)     AttributeError: 'frozenset' object has no attribute 'add'
# fst.remove(4)  AttributeError: 'frozenset' object has no attribute 'remove'

# 作为字典的key frozenset can be used as key of a dictionary (the whole set)
adict = {fst:1, 'b':2}  # works
# bdict = {st:1, 'b':2}   # TypeError: unhashable type: 'set'



# basic attributes and operation
a = [0, 1, 1, 1, 2, 3, 3, 4, 'foo', 'bar']
st = set(a)          # >>> {0, 1, 2, 3, 4, 'foo', 'bar'}
fst = frozenset(a)   # >>> frozenset({0, 1, 2, 3, 4, 'foo', 'bar'})

print(len(st))  # >>> 7
print(2 in st, 'bar' not in st)  # >>> True False

st1 = {1,2,3}
st2 = {1, 2, 'c'}
print(st1.isdisjoint(st2))  # >>> False
print(emptset.isdisjoint(emptfset))  # >>> True # for two empty set
# 如果该集合中任何一个元素都与另一个集合other中的任何一个元素都不一样（即两集合不相交），则返回True。
# 当且仅当两集合的交集为空集时，这两个集合不相交

# create a copy
st1 = {1,2,3}
st2 = st1.copy()
print(st2)  # >>> {1, 2, 3}

# subset
st1 = {1,2,3}
st2 = {4,1,5,2,6,3}
st3 = {3,2,1}
print(st1.issubset(st2))  # >>> True
print(st1.issubset(st3))  # >>> True  # even two sets are identical.
print(st1 <= st3)         # >>> True  # same function
print(st1 < st3)          # >>> False  # 判断真子集 (proper subset)

# superset
print(st2.issuperset(st1))  # >>> True
print(st2 >= st1)           # >>> True
print(st3 > st1)            # >>> False # 判断真超集 (proper superset)


# 逻辑运算

st1 = {1,2,3,4}
st2 = {3,4,5,6}
st3 = {4,5,6,7}
# union(other, ...)
# set | other | ...
# 并集
print(st1.union(st2, st3))  # >>> {1, 2, 3, 4, 5, 6, 7}
print(st1 | st2 | st3)      # >>> {1, 2, 3, 4, 5, 6, 7}

# intersection(other, ...)
# set & other & ...
# 交集
print(st1.intersection(st2, st3))  # >>> {4}
print(st1 & st2 & st3)             # >>> {4}

# difference(*others)
# set - other - ...
# 差集
print(st1.difference(st2, st3))  # >>> {1, 2}  # items in st1 but not in st2 and st3
print(st1 - st2 - st3)           # >>> {1, 2}  # same
print({1,2,3} - {1,2,3,4})       # >>> set()   # 子集-超集=空集

# symmetric_difference(other)
# set ^ other
# 对称差集
# 返回一个新的集合，元素在集合或other中，但不能在两个集合中都存在。
print(st1.symmetric_difference(st2))  # >>> {1, 2, 5, 6}
print(st1 ^ st2)                      # >>> {1, 2, 5, 6}




# other comparisons:
# frozenset基于其成员的实例与实例的set进行比较
st = set([1,2,3])          # >>> {0, 1, 2, 3, 4, 'foo', 'bar'}
fst = frozenset([1,2,3,4,5])   # >>> frozenset({0, 1, 2, 3, 4, 'foo', 'bar'})
print(st == fst)  # >>> False
print(st >= fst)  # >>> False
print(st <= fst)  # >>> True

# frozenset混合set实例的二元运算返回第一个操作数的类型。
print(st | fst)  # >>> {1, 2, 3, 4, 5}
print(fst | st)  # >>> frozenset({1, 2, 3, 4, 5})
print(st.symmetric_difference(fst))  # >>> {4, 5}
print(fst.symmetric_difference(st))  # >>> frozenset({4, 5})


# 下表列出的操作可用于set但不可用于不可变的frozenset

# update(other, ...)
# set |= other | ...
# 更新的设置，添加从所有其他的元素。
st1 = {1,2,3,4}
st2 = {'a', 'b', 'c', 'd'}

st1.update([9], [10])  # must be interable, numbers can not be directly added
print(st1)  # >>> {1, 2, 3, 4, 9, 10}
st2.update('x y z', 'lol')
print(st2)  # >>> {'c', 'l', 'a', 'b', 'd', 'x', ' ', 'z', 'y', 'o'} # 注意这里不是单独添加一个'x y z'和'lol'

st1 |= {10, 11, 13}  # one at a time
print(st1)  # >>> {1, 2, 3, 4, 9, 10, 11, 13}

# intersection_update(other, ...)
# set &= other & ...
# 更新集合,只保留集合与其他集合的交集
st1 = {1,2,3,4}
st2 = {3,4,5,6}
st1.intersection_update(st2)
print(st1)  # >>> {3, 4}  # 更改st1, 而不是新创一个交集

# difference_update(other, ...)
# set -= other | ...
# 更新集合，发现在其他元素中删除
st1 = {1,2,3,4}
st2 = {3,4,5,6}
st1.difference_update(st2)
print(st1)  # >>> {1, 2}

# symmetric_difference_update(other)
# set ^= other
# 更新集，保持只发现在任一组中，但不是在两个的元素
st1 = {1,2,3,4}
st2 = {3,4,5,6}
st1.symmetric_difference_update(st2)
print(st1) # >>> {1, 2, 5, 6}


# add(elem)
# 添加元素elem到集合。
st1 = {1,2,3,4}
st1.add(9)
print(st1)  # >>> {1, 2, 3, 4, 9}

# remove(elem)
# 从集合中移除元素elem, 如果elem不包含在集合中，提出了KeyError
st1 = {1,2,3,4}
st1.remove(3)
print(st1)  # >>> {1, 2, 4}
# st1.remove(8)  # 引发KeyError

# discard(elem)
# 从集合中移除元素elem，如果它存在
st1 = {1,2,3,4}
st1.discard(8)  #　不引发KeyError
st1.discard(1)
print(st1)  # >>> {2, 3, 4}

# pop()
# 从集合中移除并返回任意元素。如果此集合为空，则引发KeyError
st1 = {4,2,1,3}
st2 = {'a', 'b', 'c', 'd'}
st1.pop()   # 不能添加index
st1.pop()
print(st1)  # >>> {3, 4}  # 似乎数字set的pop()是从最小的数字开始pop?
# The reason it says it is arbitrary is because there is no guarantee about the ordering it will pop out.
# STOF: https://stackoverflow.com/questions/9848693/set-popping-python

st2.pop()
print(st2)  # >>> {'a', 'c', 'd'}  # string set 更随机

# clear()
# 从集合中移除所有元素。
st1 = {4,2,1,3}
st1.clear()
print(st1)  # >>> set()
