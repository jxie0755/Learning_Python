# For each test, assume all the dice are the same and are numbered from 1 to the number of sides, inclusive.
# So a 4-sided die (D4) would have an equal chance of rolling a 1, 2, 3 or 4. A 20-sided die (D20) would have an equal chance of rolling any number from 1 to 20.
# Tips: Be careful if you want to use a brute-force solution -- you could have a very, very long wait for edge cases.

# Input: Three arguments. The number of dice, the number of sides per die and the target number as integers.
# Output: The probability of getting exactly target number on a single roll of the given dice as a float.


import itertools
import math
import functools

def probability(dice_number, sides, target):
    sidenumber = list(range(1,sides+1))
    result = list(map(lambda x: sum(x), itertools.product(sidenumber, repeat=dice_number)))
    return result.count(target) / len(result)


import itertools
import math
import functools


def probability(dice_number, sides, target):
    # first get total possible permutation of all dice result
    totalp = sides ** dice_number

    # use itertools.combination to get possible combination that could end up as sum = target
    match = 0
    for i in itertools.combinations_with_replacement(range(1, sides + 1), dice_number):
        if sum(i) == target:
            # but for each combination, there is possible multiple permutations that could makes the same combination
            main = math.factorial(len(i))  # if all elements are not repeating

            # if some elements are repeating, then the possible permuation is much less.
            divi = functools.reduce(lambda x, y: x * y, map(lambda j: math.factorial(i.count(j)), set(i)))
            match += main / divi

    # at the end, output the matched number of combination that sum=target, divided by the total number of permutations
    return match / totalp

# the key to solve the problem is the calculate permutation with repeating items:
# if items are different (a=[1,2,3,4,5,6], permutation = 6!)
# if items are partially repeating (a=[1,1,2,2,2,3], permutation=6!/(2!*3!)

if __name__ == '__main__':
    #These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    print('done for small numbers')
    assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
    print('done for large numbers too')


