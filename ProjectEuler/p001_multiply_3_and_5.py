# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


def pe_001(n):
    result = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result


# This problem had a difficulty rating of 5%.

# Additional information
# This method is simple enough but may overflow when the range is large, i.e. 10000000
# A better way is to calculate [the sum of 3 divisble + sum of 5 divisible - sum of 15 divisible]

def pe_001b(n):
    # write a function to get the end number and the total number of divisible
    def sum_divisible(divisor):
        for i in range(1, divisor + 1):
            if (n - i) % divisor == 0:
                num_end = n - i
                break
        total_n = num_end // divisor
        return (divisor + num_end) * total_n // 2

    return sum_divisible(3) + sum_divisible(5) - sum_divisible(15)


if __name__ == '__main__':
    assert pe_001(10) == 23, 'below 10'
    print('answer is:')
    print(pe_001(1000))  # passed

    print()

    print('new method:')
    assert pe_001b(10) == 23, 'below 10'
    print('answer is:')
    print(pe_001b(1000))  # passed

# test for time consumed
if __name__ == '__main__':
    import timeit
    print('\npe001, original method:')
    print(timeit.repeat('pe_001(1000)', setup='from __main__ import pe_001', repeat=3, number=10000))
    print('\npe001b, new method:')
    print(timeit.repeat('pe_001b(1000)', setup='from __main__ import pe_001b', repeat=3, number=10000))
    # new method is much faser
    print(pe_001b(1000000000))  # also works for large numbers
