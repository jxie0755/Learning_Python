# P001 Multiply 3 and 5


# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


def pe_001(n1, n2, limit):
    result = 0
    for i in range(1, limit):
        if i % n1 == 0 or i % n2 == 0:
            result += i
    return result


# This problem had a difficulty rating of 5%.

# Additional information
# This method is simple enough but may overflow when the range is large, i.e. 10000000
# A better way is to calculate [the sum of 3 divisble + sum of 5 divisible - sum of 15 divisible]


def pe_001b(n1, n2, limit):
    # write a function to get the end number and the total number of divisible and then calculate the sum by using formula of Arithmetic progression

    def sum_divisible(divisor):
        num_end = (limit - 1) - (limit - 1) % divisor
        total_n = num_end // divisor
        return (divisor + num_end) * total_n // 2

    return sum_divisible(n1) + sum_divisible(n2) - sum_divisible(n1*n2)


if __name__ == '__main__':
    assert pe_001b(3, 5, 10) == 23, 'below 10'
    print(pe_001b(3, 5, 1000))
    # >>> 233168
    # passed
