# Check out this example sequence: (1, 2, 5, 3, 4, 7, 6)
# we can see here three inversions: (5,3),(5,4),(7,6)

# Input: A sequence as a tuple of integers.
# Output: The inversion number as an integer.


import itertools
def count_inversion(sequence):
    # get a sublist of all 2 elements combination
    # then get a filter list of the sets that first value is larger than second, and get the length of the list
    return len(list(filter(lambda x:x[0]>x[1], itertools.combinations(sequence, 2))))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
