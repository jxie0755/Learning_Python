# heapq module
# https://docs.python.org/3/library/heapq.html



# 这个模块提供了堆队列算法的实现，也称为优先队列算法。

# 堆是一个二叉树，它的每个父节点的值都只会小于或大于所有孩子节点（的值）。它使用了数组来实现：从零开始计数，对于所有的 k ，都有``heap[k] <= heap[2*k+1]`` 和 heap[k] <= heap[2*k+2] 。为了便于比较，不存在的元素被认为是无限大。堆最有趣的特性在于最小的元素总是在根结点：heap[0] 。
#
# 这个API与教材的堆算法实现不太一样，在于两方面：（a）我们使用了基于零开始进行索引。这使得节点和其孩子节点索引之间的关系不太直观，但是更加适合
#
# 基于这两方面，把堆看作原生的Python list也没什么奇怪的： heap[0] 表示最小的元素，同时 heap.sort() 维护了堆的不变性！



import heapq
import random

# 要创建一个堆，可以使用list来初始化为 [] ，或者你可以通过一个函数 heapify() ，来把一个list转换成堆。
# heap没有独特的数据结构, 以list形式表现,但是被称为heap的话必须确保list首先被heapify
# 以下直接用heap或者H表示被heapify的list

print('\n')
print('heapq.heapify(x)', '\nx is a list')
A = [3, 4, 1, 9, 2, 5, 8, 7]
# random.shuffle(A)
print('startting list', A)
heapq.heapify(A)
H = A[:]
print('heapified list', H)
# >> [1, 2, 4, 3, 5, 9, 7, 8, 6]
# 注意, 同样1-9的list, 随机打乱后, 由于初始排序不同可能导致生成的堆绝对顺序不同
# 但是他们都保持堆的特性, 父节点<=子节点
# 如果重复heapify, 不会有任何变化


print('\n')
print('heapq.heappop(heap)')
print(heapq.heappop(H)) # >>> 1
print(H) # >>> [2, 4, 3, 7, 9, 5, 8]
print(heapq.heappop(H)) # >>>  2
print(H) # >>> [3, 4, 5, 7, 9, 8]

# 最小值永远是heap第一个, 如果不想pop可以直接访问heap[0]

# pop改变堆的逻辑, pop顶层父节点, 假设L<R, R<b<a
#     P
#  L    R
# a b  c d
# 变成:
#     L
#  R    b
# c d  a

print('如果事先不变成heap,直接pop会如何?')
A = [6,5,4,3,2,1]
print(heapq.heappop(A)) # >>> 6
print(A) # >>> [1, 5, 4, 3, 2]
# 这样会完全变乱, 所以必须要先确保list先被heapify!!



print('\n')
print('heapq.heappush(heap, item)')
# 将 item 的值加入 heap 中，保持堆的不变性。
H = [1, 5, 3, 8, 6, 9, 7]
heapq.heappush(H, 2)
print(H) # >>> [1, 2, 3, 5, 6, 9, 7, 8]
# 优先替换左侧的元素如果能够满足要求
print()
H = [2, 3, 4, 5, 6, 7, 8]
heapq.heappush(H, 1)
print(H) # >>> [1, 2, 4, 3, 6, 7, 8, 5]



print('\n')
print('heappushpop(heap, item)')
# 将 item 放入堆中，然后弹出并返回 heap 的最小元素
# 该组合操作比先调用  heappush() 再调用 heappop() 运行起来更有效率
print('\ntest push then pop')
H = [1, 2, 4, 3, 9, 7, 8, 6]
heapq.heappush(H, 5)
print(H) # >>> [1, 2, 4, 3, 9, 7, 8, 6, 5]
heapq.heappop(H)
print(H) # >>> [2, 3, 4, 5, 9, 7, 8, 6]
print('test pushpop')
H = [1, 2, 4, 3, 9, 7, 8, 6]
print(heapq.heappushpop(H, 5)) # >>> 1
print(H) # >>> [2, 3, 4, 5, 9, 7, 8, 6]
print()

print('\ntest push then pop 2')
H = [2,3,4,5,6,7,8]
heapq.heappush(H, 1)
print(H) # >>> [1, 2, 4, 3, 6, 7, 8, 5]
heapq.heappop(H)
print(H) # >>> [2, 3, 4, 5, 6, 7, 8]
print('test pushpop 2')
H = [2,3,4,5,6,7,8]
print(heapq.heappushpop(H, 1)) # >>> 1
print(H) # >>> [2, 3, 4, 5, 6, 7, 8]
print()


print('\n')
print('heapq.heapreplace(heap, item)')
# 基本和pushpop相同逻辑,但是先pop再push
H = [2,3,4,5,6,7,8]
print(heapq.heapreplace(H, 1)) # >>> 2
print(H) # >>> [1, 3, 4, 5, 6, 7, 8]


print('\n')
print('heapq.merge(*iterables, key=None, reverse=False)')
# Merge multiple sorted inputs into a single sorted output.
# *iterable must already be a sorted
# Similar to sorted(itertools.chain(*iterables)) but returns an iterable, does not pull the data into memory all at once, and assumes that each of the input streams is already sorted (smallest to largest).
#  Returns an iterator over the sorted values.
A = [-1,-3,-5,-7]
B = [2,4,6,8]
C = heapq.merge(A, B)
print(list(C)) # >>> [-1, -3, -5, -7, 2, 4, 6, 8]
D = heapq.merge(A, B, key=lambda x:abs(x))
print(list(D)) # >>> [-1, 2, -3, 4, -5, 6, -7, 8]

# To use reverse=True, all iterables must be sorted from largest to smallest.
A = [7,5,3,1]
B = [8,6,4,2]
E = heapq.merge(A, B, reverse=True)
print(list(E)) # >>> [8, 7, 6, 5, 4, 3, 2, 1]
A = [-7,-5,-3,-1]  # 此处需要保证key处理之后还是reversely sorted, 而不是key处理之前
B = [8,6,4,2]
F = heapq.merge(A, B,  key=lambda x:abs(x), reverse=True)
print(list(F)) # >>> [8, -7, 6, -5, 4, -3, 2, -1]


print('\n')
print('heapq.nlargest(n, iterable, key=None)')
# Return a list with the n smallest elements from the dataset defined by iterable.
print('heapq.nsmallest(n, iterable, key=None)')
# Return a list with the n smallest elements from the dataset defined by iterable.

# Best for smaller values of n (len(list)). For larger values, it is more efficient to use the sorted() function.
# key is the same as used in sorted(list)
A = [8,1,6,3,4,5,2,7]
print(heapq.nlargest(5, A))  # >>> [8, 7, 6, 5, 4]  reversely sorted n-largets
print(heapq.nsmallest(5, A)) # >>> [1, 2, 3, 4, 5]  sorted n-smallest



print('\n\n')
print('Additional')
print()
print('Achieve heapsort')
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for _ in range(len(h))]
print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
# >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# This is not stable sort (break sequence of previously sorted subsequence)


print('\n')
print('Heap elements can be tuples')
# sorted(list) can't easily do this
# This is useful for assigning comparison values (such as task priorities) alongside the main record being tracked
h = []
heapq.heappush(h, (5, 'write code'))
heapq.heappush(h, (7, 'release product'))
heapq.heappush(h, (1, 'write spec'))
heapq.heappush(h, (3, 'create tests'))
print(h) # >>>  [(1, 'write spec'), (3, 'create tests'), (5, 'write code'), (7, 'release product')]

