# itertools recipes
# This is to learn a few simple functions to use itertools
# 扩展工具提供与底层工具集相同的高性能。优越的存储器性能通过一次一个处理元件来保持，而不是一次性地将整个可迭代器带入存储器。通过以有助于消除临时变量的功能样式将工具链接在一起，使代码量保持较小。在使用for循环和generator的情况下，通过优选“向量化”构造块来保持高速，这引起解释器开销。
from itertools import *

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
# stof 网友详细回答 https://stackoverflow.com/questions/47489988/what-does-python-itertools-recipe-consume-mean-at-all


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
