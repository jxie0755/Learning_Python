# Exponential complexity, most expensive type, O(2^n)
# A function that could be exponential (Tower of Hanoi) is typically a function that more than one recursive call.

def genSubset(L):
    """L as a list"""
    if len(L) == 0:
        return [[]]  # list of empty list
    smaller = genSubset(L[:-1])  # the list without last element
    extra = L[-1:]  # a list of just the last element
    new = []
    for small in smaller:
        new.append(small + extra)
    return smaller + new

if __name__ == '__main__':
    print(genSubset([1,2]))  # >>> [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    print(len(genSubset([1,2,3])))  # >>> 8
    print(len(genSubset([1,2,3,4])))  # >>> 16
    print(len(genSubset([1,2,3,4,5])))  # >>> 32
    print(len(genSubset([1,2,3,4,5,6])))  # >>> 64


# Version 2, using itertools.combinations() and a loop for different length
def genSubset2(L):
    """L as a list"""
    import itertools
    result = []
    for i in range(len(L) + 1):
        result += list(itertools.combinations(L, i))
    return result

if __name__ == '__main__':
    print(genSubset2([1,2,3]))  # >>> [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    print(len(genSubset2([1,2,3])))  # >>> 8
    print(len(genSubset2([1,2,3,4])))  # >>> 16
    print(len(genSubset2([1,2,3,4,5])))  # >>> 32
    print(len(genSubset2([1,2,3,4,5,6])))  # >>> 64
