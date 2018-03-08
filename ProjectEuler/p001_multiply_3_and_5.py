# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def pe_001(n):
    result = 0
    for i in range(1, n):
        if not i % 3 or not i % 5:
            result += i
    return result

if __name__ == '__main__':
    assert pe_001(10) == 23, 'below 10'
    print(pe_001(1000))
    print('passed')

# This problem had a difficulty rating of 5%.
