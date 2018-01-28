# Best case and worst case
def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False

# Express your answer in terms of n, the number of elements in the list L
# Best case: list is empty, so one operation, return False
# Worst case, x not in L, so go through every element in L (n operation), then check each time if e==x, (n operation), then return False (1 operation), in total: 2n+1