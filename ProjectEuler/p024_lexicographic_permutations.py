# P024 Lexicographic permutations


# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


from itertools import permutations


def lexi_perm(str_int, nth):
    """return the nth lexicographic permutation of a string of digits"""
    all = permutations(str_int)
    for i in range(nth):
        target = next(all)
    return int(''.join(target))


if __name__ == '__main__':
    assert lexi_perm('012', 4) == 120
    print(lexi_perm('0123456789', 1000000))
    # >>> 2783915460
    # passed
