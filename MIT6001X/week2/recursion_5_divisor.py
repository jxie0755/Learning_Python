# the greatest common divisor of two positive integers
# 求最大公约数

def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == b:
        print('The greatest common divisor is', 1)
        return a
    elif a <= b:
        divisor = a
        while divisor >= 0:
            if a % divisor != 0 or b % divisor != 0:
                divisor -= 1
        else:
            print('The greatest common divisor is', divisor)
            return divisor
    else:
        divisor = b
        while divisor > 0:
            if a % divisor != 0 or b % divisor != 0:
                divisor -= 1
        else:
            print('The greatest common divisor is', divisor)
            return divisor

# the recursion version
# A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors.
# Suppose that a and b are two positive integers:
# If b = 0, then the answer is a
# Otherwise, gcd(a, b) is the same as gcd(b, a % b)

def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        print('The greatest common divisor is', a)
        return a
    else:
        return gcdRecur(b, a % b)
