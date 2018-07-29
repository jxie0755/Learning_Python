# CSM02 Lists and Trees


# Write a function that takes in a list nums and returns a new list with only the primes from nums.
# Assume that is_prime(n) is defined. You may use a while loop, a for loop, or a list comprehension

def all_primes(nums):
    """return the prime numbers in a list of nums
    nums: intial list of num
    return: a new list, with only the prime numbers from nums.
    """
    return list(filter(lambda x: all(x % i != 0 for i in range(2, x)), nums))
    # assume is_prime is defined:
    # def is_prime(n):
    #     return all(n % i != 0 for i in range(2, n))
    # return list(filter(is_prime, nums))

# Write a function that takes in a list of positive integers and outputs a list of lists
# where:
# the i-th list contains the integers from 0 up to, but not including,
# the i-th element of the input list.

def list_of_lists(lst):
    """
    >>> list_of_lists([1, 2, 3])
    [[0], [0, 1], [0, 1, 2]]
    >>> list_of_lists([1])
    [[0]]
    >>> list_of_lists([])
    []
    """
    result = []
    if lst:
        for i in lst:
            result.append([i for i in range(0,i)])
    return result
