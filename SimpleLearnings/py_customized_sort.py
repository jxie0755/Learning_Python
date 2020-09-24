"""
This is to learn how to create customized sort
"""
import functools
from typing import *


# 和Java不同,这里不需要定义怎么比较,只需要定义怎么转换成一个值
def absSort(a: int) -> int:
    return a * a

if __name__ == '__main__':
    # 三者等同
    a = [-5, 4, -3, 2]
    print(max(a, key=abs))
    print(max(a, key=absSort))
    print(max(a, key=lambda x: abs(x)))
    # >>> -5

    print(sorted(a, key=abs))
    print(sorted(a, key=absSort))
    print(sorted(a, key=lambda x: abs(x)))

    # key也可以写成两者比较的函数,需要调用functools.cmp_to_key
    print(sorted(a, key=functools.cmp_to_key(lambda x, y: abs(x) - abs(y))))
    # >>> [2, -3, 4, -5]



# 更复杂点的intGrid排序, 需要对比两个值, 返回-1,0,1来比较x和y的关系
# x < y, return -1
# x == y, return 0
# x > y, return 1

def intGridCompare(x: List[int], y: List[int]) -> int:
    min_length = min(len(x), len(y))
    for i in range(min_length):
        if x[i] < y[i]:
            return -1
        elif x[i] > y[i]:
            return 1

    if len(x) == len(y):
        return 0
    elif len(x) < len(y):
        return -1
    else:
        return 1

if __name__ == '__main__':
    grid = [
        [3, 2, 1],
        [1, 3, 2],
        [2, 3, 1],
        [2, 1, 3],
        [1, 2, 3],
        [3, 1, 2]
    ]

    # 自定义compare同样需要调用unctools.cmp_to_key(cmp)来做key
    print(sorted(grid))
    print(sorted(grid, key=functools.cmp_to_key(intGridCompare)))
    # >>> [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
