# itertools recipes
# This is to learn a few simple functions to use itertools
# 扩展工具提供与底层工具集相同的高性能。优越的存储器性能通过一次一个处理元件来保持，而不是一次性地将整个可迭代器带入存储器。通过以有助于消除临时变量的功能样式将工具链接在一起，使代码量保持较小。在使用for循环和generator的情况下，通过优选“向量化”构造块来保持高速，这引起解释器开销。
from itertools import *

def take(n, iterable):
    """Return first n items of the iterable as a list"""
    return list(islice(iterable, n))
lst = [1, 2, 3, 4, 5]
print(take(3, lst))  # >>> [1, 2, 3]


def tabulate(function, start=0):
    """Return function(0), function(1), ...."""
    return map(function, count(start))
x = (tabulate(lambda x:x*2, 0))
for i in range(8):
    print(next(x) * next(x))  # 注意这不等于 next(x)**2



