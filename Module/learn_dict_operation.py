print('dict(**kwarg)')
print('dict(mapping, **kwarg)')
print('dict(iterable, **kwarg)')

# 一个mapping对象将hashable的值映射到任意对象。映射是可变对象。目前只有一种标准映射类型，那就是字典Dictionary

# 字典的键几乎是任意值。值是不能hashable，也就是包含列表、字典或其它可变类型的值（它们通过值而不是对象ID进行比较）不可以用作键。
# dd = {[1,2,3]:'abc', [2,3,4]:'def'}  # >>> TypeError: unhashable type: 'list'


# 用于键的数值类型遵守数值比较的正常规则：如果两个数字的比较结果相等（如1.0和1），那么它们可以用于互相索引相同的词典条目。
# （注意，由于计算机存储的是浮点数的近似值，因此将浮点数作为键值是不明智的。)
dd = {1:'abc', 2:'def'}
print(hash(1) == hash(1.00))   # >>> True  # 1和1.0是相同hash值
print(dd[1] == dd[1.0])        # >>> True  # 所以它们会映射相同的键值



# 字典可以通过放置一个逗号分隔的key: value对列表于花括号中创建或通过dict构造函数创建。
# 通过{}创建, 可以是空dict (因为set不能这么被创造)
dd = {}
print(type(dd))  # >>> <class 'dict'>

# class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)

# 通过dict创建,必须是组成对的值
print(dict(a=4,b=5,c=None))                   # >>> {'a': 4, 'b': 5, 'c': None}  # from **kwargs
k, v = ['a', 'b', 'c'], [4,5,None]
print(dict(zip(k, v)))                        # >>> {'a': 4, 'b': 5, 'c': None}  # from zip(), must be 2 groups
print(dict([('a', 4),('b', 5),('c', None)]))  # >>> {'a': 4, 'b': 5, 'c': None}  # from iterable, must be 2 groups
print(dict({'a': 4, 'b': 5, 'c': None}))      # >>> {'a': 4, 'b': 5, 'c': None}  # from mapping



# basic dict operation
dd = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(len(dd))  # >>> 5

print(dd['b'])  # >>> 2 # 引发 KeyError 如果键不在映射中

dd['b'] = 22 # 设置d[key]的值为value
print(dd)  # >>> {'a': 1, 'b': 22, 'c': 3, 'd': 4, 'e': 5}

del dd['e']
print(dd)  # >>> {'a': 1, 'b': 22, 'c': 3, 'd': 4}  # 引发KeyError如果键不在映射中

print('c' in dd)      # >>> True
print('f' not in dd)  # >>> True

print(list(iter(dd))) # >>> ['a', 'b', 'c', 'd']  # 这是iter(d.keys())的快捷方式

ddd = dd.copy()
print(ddd)  # >>> {'a': 1, 'b': 22, 'c': 3, 'd': 4}  # create a copy

# classmethod fromkeys(seq[, value])
seq = ('name', 'age', 'sex')
dict1 = dict.fromkeys(seq)
print(dict1)   # >>> {'name': None, 'age': None, 'sex': None}
dict2 = dict.fromkeys(seq, 10)
print(dict2)   # >>> {'name': 10, 'age': 10, 'sex': 10}

# get(key[, default])
# 如果 key 在字典里，返回 key 的值，否则返回 default 值。
# 如果 default 未给出，它默认为 None，此方法永远不会引发 KeyError。
dd = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dd.get('b', '123'))  # >>> 2     # 相当于 d['b']
print(dd.get('f'))         # >>> None  # 相当于 d['f'], 但是不会引发error
print(dd.get('f', '123'))  # >>> 123   # 引发default



# dict.items(), dict.keys(), dict.values()
# 返回字典项目的新视图, 注意这个类似容器,不是iterator也不是generator,不存在consume的问题
print(dd.items())    # >>> dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
print(dd.keys())     # >>> dict_keys(['a', 'b', 'c', 'd', 'e'])
print(dd.values())   # >>> dict_values([1, 2, 3, 4, 5])

dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
values = dishes.values()

# iteration
n = 0
for val in values:
    n += val
print(n) # >>> 504

# keys and values are iterated over in the same order
print(list(keys))    # >>> ['eggs', 'bacon', 'sausage', 'spam']
print(list(values))  # >>> [2, 1, 1, 500]

# view objects are dynamic and reflect dict changes
del dishes['eggs']
del dishes['sausage']
print(list(keys))  # >>> ['spam', 'bacon']

# keys() are considered as a set, so accept set operations
print(keys & {'eggs', 'bacon', 'salad'})  # >>> {'bacon'}
print(keys ^ {'sausage', 'juice'})        # >>> {'juice', 'sausage', 'bacon', 'spam'}



# popitem()
# 如果字典为空，调用popitem()将引发一个KeyError
dd = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
dd.popitem()  # in python 3.6 popitem() pop out的last item
print(dd)

# sequence of dictionary
dd = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
ddd = dict(sorted(dd.items()))  # >>> {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(ddd)

# print([(k, v) for k, v in reversed(ddd.items())])
# >>> TypeError: 'dict_items' object is not reversible
# does not work like collections.OrderedDict

# setdefault(key[, default])
# 如果key在字典中，则返回其值。如果没有，则插入值为default的key，并返回default. default默认为None
print(ddd.setdefault('b'))  # >>> 2
print(ddd.setdefault('x'))  # >>> None
print(ddd)  # >>> {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'x': None}
print(ddd.setdefault('y', 'YYY'))  # >>> YYY
print(ddd)  # >>> {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'x': None, 'y': 'YYY'}


# update([other])
# 依据other更新词典的键/值对，覆盖现有的键. 返回None
# update()接受另一个字典对象或可迭代的键/值对（如元组或其它长度为2的可迭代对象
ddd.update([('x', 'X-3'),('y', 'Y-3')])
print(ddd)  # >>> {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'x': 'X-3', 'y': 'Y-3'}
bbb = {'Denis': 55, 'Xie': 66}
ddd.update(bbb)
print(ddd)  # >>> {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'x': 'X-3', 'y': 'Y-3', 'Denis': 55, 'Xie': 66}
# 如果指定的是关键字参数，那么字典使用这些键/值对更新
ddd.update(a=None, b=None, c=333)
print(ddd)  # >>. {'a': None, 'b': None, 'c': 333, 'd': 4, 'e': 5, 'x': 'X-3', 'y': 'Y-3', 'Denis': 55, 'Xie': 66}

ddd.clear()
print(ddd)  # >>> {}
