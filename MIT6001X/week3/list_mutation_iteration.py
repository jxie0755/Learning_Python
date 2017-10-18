# YOU SHOULD AVOID MUTATING A LIST WHEN ITERATING OVER IT!!!

def remove_dups(L1, L2):
    # L1_copy = L1[:]      # add this line could avoid the problem
    for e in L1:
        if e in L2:
            L1.remove(e)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2)

print(L1)
# >>> [2, 3, 4]
# not as expected to be [3, 4]

# python uses an internal counter to keep track of index when in loop
# mutating changes the list during iteration changed list length, but index counter was not updated



