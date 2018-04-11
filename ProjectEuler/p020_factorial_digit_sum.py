# P020 Factorial digit sum


# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!


def fact_digit_sum(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return sum([int(i) for i in str(result)])


if __name__ == '__main__':
    assert fact_digit_sum(10) == 27, 'regular'
    print(fact_digit_sum(100))
    # >>> 648
    passed
