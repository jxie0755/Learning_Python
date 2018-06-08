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
    """L is a sorted list"""
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




# Sorting algorithm
# Monkey Sort (aka bogosort, stupid sort, slowsort, permutation sort, shotgun sort)
import random
def bogo_sort(L):
    # write an internal function to define what is the sort target
    def is_sorted(L):
        index = 1
        while index < len(L):
            if L[index - 1] > L[index]:
                return False
            index += 1
        return True
    # randomly shuffle the list until it reaches to target
    count = 0
    while not is_sorted(L):
        random.shuffle(L)
        count += 1
    print(L, 'shuffled', count, 'times')

# if __name__ == '__main__':
#     print('bogo sort')
#     bogo_sort([1, 5, 3, 8, 4, 9, 6, 2, 7])

# Bubble Sort
def bubble_sort(L):
    """to sort to from small to large"""
    swap = False
    count = 0
    while not swap:  # while loop for multiple passes O(n)
        swap = True
        for j in range(1, len(L)):  # for loop for doing comparisons O(n)
            if L[j-1] > L[j]:
                swap = False

                # temp = L[j]
                # L[j] = L[j-1]
                # L[j-1] = temp
                # simplify to:
                L[j-1], L[j] = L[j], L[j-1]

                count += 1
    print(L, 'swapped', count, 'times')
# complexity is O(n^2), while n = len(L)

if __name__ == '__main__':
    print('bubble sort')
    bubble_sort([1, 5, 3, 8, 4, 9, 6, 2, 7])
    bubble_sort([3, 3, 2, 1, 4, 3, 2])  # works on repeated item list

# Selection Sort
def selection_sort(L):  # self try, O(n)
    index = 0
    while index < len(L):
        minimum_index = L.index(min(L[index:]))
        L[index], L[minimum_index] = min(L[index:]), L[index]
        index += 1
    print(L)
    # does not apply to list with repeated item because index will be wrong

def selection_sort(L): # Version 2, MIT method
    # the idea is to divide the list into two part and move smallest item to first half
    # the way to find smallest element is dynamic, not by one swap
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
    print(L)
    # this could avoid the index problem, but more swaps
    # still O(n ^ 2), but more efficient than bubble sort, because the list gets shorter in every loop

def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp
    # this is the version that use only one swap for each loop
    # it creates an internal variable of index for the minimum in the rest of the list
    # this index will keep updating until finish one round of looping, and swap once if needed

if __name__ == '__main__':
    print('selection sort')
    selection_sort([1, 5, 3, 8, 4, 9, 6, 2, 7])
    selection_sort([3, 3, 2, 1, 4, 3, 2])


# Comparison between bubble sort and selection sort
def bub_Sort(L): # bubble sort
    """ L, list with unique elements """
    clear = False
    count = 0
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
                count += 1
    print('swapped', count, 'times')

def sel_Sort(L):
    """ L, list with unique elements """
    count = 0
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
                count += 1
            j += 1
    print('swapped', count, 'times')


if __name__ == '__main__':
    print('bubble sort vs. selection sort')
    bub_Sort([1, 5, 3, 8, 4, 9, 6, 2, 7])  # >>> 13 times
    sel_Sort([1, 5, 3, 8, 4, 9, 6, 2, 7])  # >>> 13 times
    # They both swap the value same amount of times


# Merge Sort
def merge(left, right):  # O(n), n as the length of the longer list
    """both left and right are sorted list """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)
    # Divide part: Break down problem into half, O(log(n))
    # Each divide, merge O(n)
    # Overall O(n*log(n)), better than O(n^2)

if __name__ == '__main__':
    L = [1, 5, 3, 8, 4, 9, 6, 2, 7]
    print(merge_sort([1, 5, 3, 8, 4, 9, 6, 2, 7]))
    print(L)  # this method takes extra space
