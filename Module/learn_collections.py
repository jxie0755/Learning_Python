import collections

print()
print('collections.ChainMap(*maps)')
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
print('collections.Counter([iterable-or-mapping])')

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
print(c)  # >>> Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

# 同理可以update,也就是增加
c = collections.Counter(a=4, b=2, c=0, d=-2)
d = collections.Counter(a=1, b=2, c=3, d=4)
c.update(d)
print(c)  # >>> Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2})

