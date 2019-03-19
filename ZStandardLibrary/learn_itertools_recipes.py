# itertools recipes
# https://docs.python.org/3/library/itertools.html#itertools-recipes

# This is to learn a few simple functions to use itertools
# 扩展工具提供与底层工具集相同的高性能。优越的存储器性能通过一次一个处理元件来保持，而不是一次性地将整个可迭代器带入存储器。通过以有助于消除临时变量的功能样式将工具链接在一起，使代码量保持较小。在使用for循环和generator的情况下，通过优选“向量化”构造块来保持高速，这引起解释器开销。
from itertools import *
from operator import *
import random

print()
print('take')
def take(n, iterable):
    """Return first n items of the iterable as a list"""
    return list(islice(iterable, n))
lst = [1, 2, 3, 4, 5]
print(take(3, lst))  # >>> [1, 2, 3]


print()
print('tabulate')
def tabulate(function, start=0):
    """Return function(0), function(1), ...."""
    return map(function, count(start))
x = (tabulate(lambda x:x*2, 0))
for i in range(8):
    print(next(x) * next(x))  # 注意这不等于 next(x)**2


print()
print('tail')
import collections
def tail(n, iterable):
    """Return a list over the last n items"""
    return list(iter(collections.deque(iterable, maxlen=n)))
lst = [1, 2, 3, 4, 5]
print(tail(3, lst))  # >>> [3,4,5]


print()
print('consume')
def consume(iterator, n):
    """"Advance the iterator n-steps ahead. If n is none, consume entirely."""
    # use functions that consume iterators at C speed
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)
aa = iter([1,2,3,4,5])
print(consume(aa, 2)) # The purpose for this function is not output None
print(next(aa))  # >>> 3, because consume(aa, 2) iterated the first 2 elements, so next(aa) gives the 3rd elements
print(list(aa))  # >>> [4, 5]
# iterator is needed because this could change aa after the consume and next().
# this is the true purpose for this function, to jump to the nth elements of an iterator with no cost.
# STOF 网友详细回答 https://stackoverflow.com/q/47489988/8435726


print()
print('nth')
def nth(iterable, n, default=None):
    """Returns the nth item or a default value"""
    return next(islice(iterable, n, None), default)
aa = iter([1, 2, 3, 4])
print(nth(aa, 2, 99))   # >>> 3   由于aa[2]存在一个值=3, 所以返回3
print(nth(aa, 10))  # >>> 99  由于aa[10]不存在, 所以返回default value=99, 若不指定,则返回None,也不至于StopIteration


print()
print('all_equal')
def all_equal(iterable):
    """Returns True if all the elements are equal to each other"""
    g = groupby(iterable)
    print(not next(g))
    return next(g, True) and not next(g, False)

aa = ['a', 'a', 'a']
print(all_equal(aa))  # >>> True


print()
print('quantify')
def quantify(iterable, pred=bool):
    """Count how many times the predicate is true"""
    return sum(map(pred, iterable))
aa = [1,2,0,4]
print(quantify(aa))  # >>> 3, 因为0不为True,所以一共3个True
aa = [1,2,0,4]
print(sum(map(lambda x: bool(x), aa)))  # 约等于这个


print()
print('padnone')
def padnone(iterable):
    """Returns the sequence elements and then returns None indefinitely

    Useful for emulating the behavior of the built-in map() function
    """
    return chain(iterable, repeat(None))
aa = padnone([1,2,3])
for i in range(5):
    print(next(aa))
# >>>
# 1
# 2
# 3
# None
# None


print()
print('ncycles')
def ncycles(iterable, n):
    """Returns the sequence elements n times"""
    return chain.from_iterable((repeat(tuple(iterable), n)))
print(list(ncycles([1,2,3,4], 3)))
# >>> [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]


print()
print('dotproduct(vec1, vec2)')
import operator
def dotproduct(vec1, vec2):
    return sum(map(operator.mul, vec1, vec2))
a = [1, 2, 3]
b = [7, 8, 9]
print(dotproduct(a, b))
# >>> equal to 1*7+2*8+3*9 = 50


print()
print('flatten(listOfLists)')
def flatten(listOfLists):
    """Flatten one level of nesting"""
    return chain.from_iterable((listOfLists))
a = [[1,2,3], ['a', 'b', 'c'], [7, 8, 9]]
print(list(flatten(a)))


print()
print('repeatfunc(func, times=None, *args)')
import random
def repeatfunc(func, times=None, *args):
    """Repeat calls to func with specified arguments"""
    if times is None:
        return starmap(func, repeat(args))
    return starmap(func, repeat(args, times))
print(list(repeatfunc(lambda x: x**2, 3, 5)))
# >>> [25, 25, 25]
print(list(repeatfunc(lambda x,y: x+y, 3, 5, 6)))
# >>> [11, 11, 11]
print(list(repeatfunc(random.random, 3)))
# >>> [list of 3 random numbers]


print()
print('pairwise(iterable)')
def pairwise(iterable):
    """s -> (s0, s1), (s1, s2), (s2, s3), ..."""
    a, b = tee(iterable)
    next(b, None)
    # next(b, None) 可以继续间隔
    # consume(b, 3) 或者甚至利用consume跳过任意间隔
    return zip(a, b)
print(list(pairwise('abcdefg')))
# >>> [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f'), ('f', 'g')]


print()
print('grouper(iterable, n, fillvalue=None)')
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

print([str(x) + str(y) + str(z) for x,y,z in grouper('ABCDEFG', 3, 'x')])
# >>> ['ABC', 'DEF', 'Gxx']


print()
print('roundrobin(*iterables)')
def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    pending = len(iterables)
    nexts = cycle(iter(it).__next__ for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = cycle(islice(nexts, pending))

print(list(roundrobin('ABC', '23', 'D')))
# >>> ['A', '2', 'D', 'B', '3', 'C']  # cycle in sequence of index of each item


print()
print('partition(pred, iterable)')
def partition(pred, iterable):
    'Use a predicate to partition entries into false entries and true entries'
    t1, t2 = tee(iterable)
    return filterfalse(pred, t1), filter(pred, t2)
for i in partition(lambda x: x%2 != 0, range(10)):
    print(list(i))
# >>>
# [0, 2, 4, 6, 8] False first
# [1, 3, 5, 7, 9] True second
# 相当于filter, filterfalse一起使用, 关键是tee的使用,把一个iterable复制成两个,分别迭代


print()
print('powerset(iterable)')
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

print(list(powerset(['a', 'b', 'b']))) # 不忽略重复item
# >>> [(), ('a',), ('b',), ('b',), ('a', 'b'), ('a', 'b'), ('b', 'b'), ('a', 'b', 'b')]
# 相当于找出一个iterable所有长度的组合, 用tuple整理
lst = list(powerset(['a', 'b', 'c', 'd']))
group_l = groupby(lst,key=len)
for k, v in group_l:
    print(k, list(v))
# >>>
# 0 [()]
# 1 [('a',), ('b',), ('c',), ('d',)]
# 2 [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]
# 3 [('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'c', 'd'), ('b', 'c', 'd')]
# 4 [('a', 'b', 'c', 'd')]


print()
print('unique_everseen(iterable, key=None)')
def unique_everseen(iterable, key=None):
    "List unique elements, preserving order. Remember all elements ever seen."
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element

print(list(unique_everseen('EAAAABBBCCDAABBB')))
# >>> ['E', 'A', 'B', 'C', 'D']
# 相当于set,自带顺序保留方式
x = 'EAAAABBBCCDAABBB'
print(sorted(set(x), key=x.index))
# >>> ['E', 'A', 'B', 'C', 'D']
print(list(unique_everseen(x, str.lower)))
# 由于使用key,把所有字符都规格化,所以不管是upper还是lower都是一个效果
# >>> ['E', 'A', 'B', 'C', 'D']


print()
print('unique_justseen(iterable, key=None)')
def unique_justseen(iterable, key=None):
    "List unique elements, preserving order. Remember only the element just seen."
    return map(next, map(itemgetter(1), groupby(iterable, key)))

print(list(unique_justseen('AAAABBBCCDAABBB')))
# >>> ['A', 'B', 'C', 'D', 'A', 'B']
print(list(unique_justseen('ABBCcAD', str.lower)))
# >>> ['A', 'B', 'C', 'A', 'D']
print(list(unique_justseen('ABBCcAcD', str.lower)))
# >>> ['A', 'B', 'C', 'A', 'c', 'D']  # justseen不会过滤掉不连续的小写c


print()
print('iter_except(func, exception, first=None)')
def iter_except(func, exception, first=None):
    """ Call a function repeatedly until an exception is raised.
    Converts a call-until-exception interface to an iterator interface.
    Like builtins.iter(func, sentinel) but uses an exception instead
    of a sentinel to end the loop.
    """
    try:
        if first is not None:
            yield first()            # For database APIs needing an initial cast to db.first()
        while True:
            yield func()
    except exception:
        pass
s = [1,2,3,4]
result = []
for i in iter_except(s.pop, IndexError):
    result.append(i)
print(result)
# >>> [4, 3, 2, 1]


print()
print('first_true(iterable, default=False, pred=None)')
def first_true(iterable, default=False, pred=None):
    """Returns the first true value in the iterable.
    If no true value is found, returns *default*
    If *pred* is not None, returns the first item
    for which pred(item) is true.
    """
    return next(filter(pred, iterable), default)
print(first_true(['','b','c'], 'x'))  # >>> b
print(first_true(['', 0, None], 'x'))  # >>> x
print(first_true([0,-1,2], 'x', lambda x:x**2)) # >>> -1


print()
print('random_product(*args, repeat=1)')
def random_product(*args, repeat=1):
    "Random selection from itertools.product(*args, **kwds)"
    pools = [tuple(pool) for pool in args] * repeat
    return tuple(random.choice(pool) for pool in pools)

print(random_product('abc'))
# >>> ('a',) or ('b',) or ('c',)
print(random_product('abc', repeat=2))
# >>> ('x', 'y') same above, x and y could be any one of 'a', 'b', 'c'
print(random_product('abc', 'def'))
# >>> ('x', 'y')  x could be any one of 'a', 'b', 'c', y from 'd', 'e', 'f'
print(random_product('abc', 'def', repeat=2))
# >>> ('x', 'y', 'x', 'y') x could be any one of 'a', 'b', 'c', y from 'd', 'e', 'f'


print()
import random
print('random_permutation(iterable, r=None)')
def random_permutation(iterable, r=None):
    "Random selection from itertools.permutations(iterable, r)"
    pool = tuple(iterable)
    r = len(pool) if r is None else r   # r <= len(iterable)
    return tuple(random.sample(pool, r))
print(random_permutation('abc'))
# >>> ('a','b', 'c') or ('b', 'a', 'c') or ('c', 'a', 'b') or any permutation of 'a', 'b', 'c'
print(random_permutation('abc', r=2))
# >>> ('b', 'a') or pick 2 out of 'a', 'b', 'c' and random permutation


print()
print('random_combination(iterable, r)')
def random_combination(iterable, r):
    "Random selection from itertools.combinations(iterable, r)"
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.sample(range(n), r))
    return tuple(pool[i] for i in indices)

print(random_combination('dcba', r=3))
# >>> ('d', 'c', 'a') or pick 3 out of 'd', 'c', 'b', 'a' and random combinations.
# since the sequence is not important anymore, the tuple will follow the order of iterable index.


print()
print('random_combination_with_replacement(iterable, r)')
def random_combination_with_replacement(iterable, r):
    "Random selection from itertools.combinations_with_replacement(iterable, r)"
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.randrange(n) for i in range(r))
    return tuple(pool[i] for i in indices)

print(random_combination_with_replacement('123', r=3))
# >>> ('2', '3', '3') same random combination, but allow repeat elements.
