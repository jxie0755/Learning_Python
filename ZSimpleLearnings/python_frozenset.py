# frozenset是冻结的集合，它是不可变的，存在哈希值，好处是它可以作为字典的key，也可以作为其它集合的元素。
# 缺点是一旦创建便不能更改，没有add，remove方法。

a = [0, 1, 1, 1, 2, 3, 3, 4]
fst = frozenset(a)
st = set(a)
print(fst == st)  # >>> True
print(st)  # >>> {0, 1, 2, 3, 4}

st.add(9)
st.remove(4)
print(st)  # >>> {0, 1, 2, 3, 9}

# fst is immutable, these editing does not work with fst
# fst.add(9)     AttributeError: 'frozenset' object has no attribute 'add'
# fst.remove(4)  AttributeError: 'frozenset' object has no attribute 'remove'

# frozenset can be used as key of a dictionary

adict = {fst:1, 'b':2} # works  
bdict = {st:1, 'b':2}  # TypeError: unhashable type: 'set'
