# P007 1001st prime


# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?


# Brutal force method
def prime(n):
    """return the nth prime number
    start from 2 as the first prime number
    2, 3, 5, 7, 11, and 13, so 13 is the 6th number
    """

    sample, count = 2, 1
    while count != n:
        sample += 1
        if all(sample % divisor != 0 for divisor in range(2, int(sample**0.5) + 1)):
            count += 1
    return sample

if __name__ == '__main__':
    assert prime(1) == 2, 'starting point'
    assert prime(6) == 13, 'simple case'
    print(prime(10001))
    # >>> 104743
    # passed
