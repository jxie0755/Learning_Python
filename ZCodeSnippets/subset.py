# a recursive function to generate all sub-list of a list
def genSubset(L):
    """L as a list"""
    res = []
    if len(L) == 0:
        return [[]]  # list of empty list
    smaller = genSubset(L[:-1])  # the list without last element
    extra = L[-1:]  # a list of just the last element
    new = []
    for small in smaller:
        new.append(small + extra)
    return smaller + new

if __name__ == '__main__':
    print(genSubset([1,2,3]))  # >>> [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

def subset_SL(L):  # basically same idea as substring
    result = []
    for lenth in range(1, len(L) + 1):
        for start in range(len(L) - lenth + 1):
            result.append(L[start:start + lenth])
    return result

if __name__ == '__main__':
    print(subset_SL([1,2,3,4]))
# >>> [[1], [2], [3], [4], [1, 2], [2, 3], [3, 4], [1, 2, 3], [2, 3, 4], [1, 2, 3, 4]]

def subset_LS(L):
    result = []
    for lenth in range(len(L), 0, -1):
        for start in range(len(L) - lenth + 1):
            result.append(L[start:start + lenth])
    return result

if __name__ == '__main__':
    print(subset_LS([1,2,3,4]))
# >>> [[1, 2, 3, 4], [1, 2, 3], [2, 3, 4], [1, 2], [2, 3], [3, 4], [1], [2], [3], [4]]

def sub_seq(L):
    result = []
    for start in range(len(L)):
        for end in range(start+1, len(L)+1):
            result.append(L[start:end])
    return result

if __name__ == '__main__':
    print(sub_seq([1,2,3,4]))
# >>> [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [2], [2, 3], [2, 3, 4], [3], [3, 4], [4]]
