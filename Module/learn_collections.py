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
print(chain.maps)  # >>> [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}], a list
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
