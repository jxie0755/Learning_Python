# Lecture 2

# Search algorithm
# Linear search
def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found

# must look through all elements
# O(n)


# Linear search (of sorted list)
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:  # if sorted, we can break the loop earlier
            return False
    return False

# O(n)

# Bisection search (of sorted list)

# Version 1, recursive way
def bi_search(L, e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e

    half = len(L) // 2
    if L[half] > e:
        return bi_search(L[:half], e)
    else:
        return bi_search(L[half:], e)

# O(log(n)), where n = len(L), but create new slices of L many times

# Version 2, regular bisection search method
def bi_search2(L, e):
    if L[-1] == e:  # edge case for the last item
        return True

    low, high = 0, len(L) - 1
    index = (low + high) // 2
    while high - low > 0:
        print(low, high, index)
        if e < L[index]:
            high = index
        elif e > L[index]:
            low = index
        else:
            return True
        index = (high + low) // 2
    return False

# O(log(n)) and no need for extra space
if __name__ == '__main__':
    L = list(range(100))
    print(bi_search2(L, 99))
    print(bi_search([], 3))

# MIT version (too comlicated)
def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:  # nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid -1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)

if __name__ == '__main__':
    L = list(range(100))
    print(bisect_search2(L, 99))


# Monkey Sort (aka bogosort, stupid sort, slowsort, permutatio sort, shotgun sort)
def is_sorted(L):
    pass

import random
def bogo_sort(L):
    while not is_sorted(L):
        random.shuffle(L)

# Bubble Sort
def bubble_sort(L):
    swap = False
    while not swap:  # while loop for multiple passes O(n)
        swap = True
        print(L)
        for j in range(1, len(L)):  # for loop for doing comparisons O(n)
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
# complexity is O(n^2), while n = len(L)

if __name__ == '__main__':
    bubble_sort([1,5,3,8,4,9,6,2])


