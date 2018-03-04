# Required Questions
print('\nQ1: WWPD: Veritasiness')
# python3 ok -q short_circuiting -u

if __name__ == '__main__':
    print(True and 13)  # >>> 13
    print(False or 0)   # >>> 0
    print(not 10)       # >>> False
    print(not None)     # >>> True
    print()
    # print(True and 1 / 0 and False)     # >>> ZeroDivisionError
    print(True or 1 / 0 or False)       # >>> True
    print(True and 0)                   # >>> 0
    print(False or 1)                   # >>> 1
    print(1 and 3 and 6 and 10 and 15)  # >>> 15
    print(0 or False or 2 or 1 / 0)     # >>> 2
    print()
    print(not 0)         # >>> True
    print((1+1) and 1)   # >>> 1
    # print((1/0) or True)  # ZeroDivisionError  # Still have to evaluate <left> even if returning <right>
    print((True or False) and False)  # >>> False

# Q2 Loops
print('\nQ2: WWPD: Loops')
# python3 ok -q loops -u

if __name__ == '__main__':
    print('answers hidden')
    # n = 3
    # while n >= 0:
    #     n -= 1
    #     print(n)
    # >>>
    # 2
    # 1
    # 0
    # -1

if __name__ == '__main__':
    print('answers hidden')
    # n = 4
    # while n > 0:
    #     n += 1
    #     print(n)
    # >>>
    # 5
    # 6
    # 7
    # ...forever continue

if __name__ == '__main__':
    print('answers hidden')
    # def go(n):
    #     if n % 2 != 0:
    #         print(n / 2)
    #         return
    #     while n > 0:
    #         print(n)
    #         n = n // 2
    # go(4)
    # >>>
    # 4
    # 2
    # 1
    # go(5)
    # >>>
    # 2.5

if __name__ == '__main__':
    print('answers hidden')
    # zero = 2
    # while zero != 0:
    #    zero = zero // 2
    #    print(zero)
    # >>>
    # 1
    # 0

if __name__ == '__main__':
    print('answers hidden')
    # positive = 28
    # while positive:
    #     print("positive?")
    #     positive -= 3
    # >>>
    # positive? (28)
    # positive? (25)
    # positive? (22)
    # positive? (19)
    # positive? (16)
    # positive? (13)
    # positive? (10)
    # positive? (7)
    # positive? (4)
    # positive? (1)
    # positive? (-2)
    # ...continue forever

if __name__ == '__main__':
    print('answers hidden')
    # positive = -9
    # negative = -12
    # while negative:
    #     if positive:
    #         print(negative)
    #     positive += 3
    #     negative += 3
    # >>>
    # -12 (p=-6, n=-9)
    # -9 (p=-3, n=-6)
    # -6 (p=0, n=-3)
    #    (p=3, n=0)
    # end

# Coding practice
print('\nCoding Practice')

print('\nQ3: Repeated')
# Implement the repeated function, which takes a one-argument function f, a positive integer n, and a parameter x. It returns the result of composing, or applying, f n times on x, i.e., f(f(...f(x)...)).
def repeated(f, n, x):
    """Returns the result of composing f n times on x.

    >>> def square(x):
    ...     return x * x
    ...
    >>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    >>> repeated(square, 1, 4)  # square(4)
    16
    >>> repeated(square, 6, 2)  # big number
    18446744073709551616
    >>> def opposite(b):
    ...     return not b
    ...
    >>> repeated(opposite, 4, True)
    True
    >>> repeated(opposite, 5, True)
    False
    >>> repeated(opposite, 631, 1)
    False
    >>> repeated(opposite, 3, 0)
    True
    """
    for i in range(n):
        x = f(x)
    return x

# python3 ok -q repeated
print('passed')


print('\nQ4: Sum Digits')
# Write a function that takes in a nonnegative integer and sums its digits. (Using floor division and modulo might be helpful here!)
def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    # use nunber method, avoid string method at this time
    result = 0
    while n > 0:
        result += n % 10
        n = n // 10
    return result

# python3 ok -q sum_digits
print('passed')


print('\nQ5: Double Eights')
# Write a function that takes in a number and determines if the digits contain two adjacent 8s.
def double_eights(n):
    """Return true if n has two eights in a row.

    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    # use nunber method, avoid string method at this time
    count = 0
    while n > 0:
        digit = n % 10
        if digit == 8:
            count += 1
        elif digit != 8:
            count = 0
        if count == 2:
            return True
        n = n // 10
    return False

# python3 ok -q double_eights
print('passed')
