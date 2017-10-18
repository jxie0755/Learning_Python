# YOU SHOULD AVOID MUTATING A LIST WHEN ITERATING OVER IT!!!

def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2)

print(L1)
# >>> [2, 3, 4]
# not as expected to be [3, 4]


