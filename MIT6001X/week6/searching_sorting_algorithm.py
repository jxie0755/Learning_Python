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

L = list(range(100))
print(bi_search2(L, 50))

