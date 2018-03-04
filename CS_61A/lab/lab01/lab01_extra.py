# Optional Questions
print('\nOptional Questions')
print('\nQ6: WWPD: Truthiness')
print(0 or True)                   # >>> True
print(not '' or not 0 and False)   # >>> True # 注意运算优先级
print(13 and False)                # >>> False
print()
print(False or 1)           # >>> True but actually show the value 1
# print('' or 1 and 1/0)      # >>> Error
print(not 0 and 12 or 0)    # >>> True but actually show the value 12


print('\nQ7: WWPD: What If?')

def xk(c, d):
    if c == 4:
        return 6
    elif d >= 4:
        return 6 + 7 + c
    else:
        return 25
print('\nxk')
print(xk(10, 10))  # >>> 23
print(xk(10, 6))   # >>> 23
print(xk(4, 6))    # >>> 6
print(xk(0, 0))    # >>> 25


def how_big(x):
    if x > 10:
        print('huge')
    elif x > 5:
        return 'big'
    elif x > 0:
        print('small')
    else:
        print("nothin'")

print('\nhow_big')
how_big(7)   # >>> return 'big'  # terminal will still show the return as the actuall string
how_big(12)  # >>> huge   # when print, it will ingore the "'"
how_big(1)   # >>> small
how_big(-1)  # >>> nothin'


def so_big(x):
    if x > 10:
        print('huge')
    if x > 5:
        return 'big'
    if x > 0:
        print('small')
    print("nothin'")

print('\nso_big')
so_big(7)   # >>> return 'big'
so_big(12)  # >>> huge and return 'big'
so_big(1)   # >>> small and nothin'


def ab(c, d):
    if c > 5:
        print(c)
    elif c > 7:
        print(d)
    print('foo')

print('\nab')
ab(10, 20)  # >>> 10 and foo


def bake(cake, make):
    if cake == 0:
        cake = cake + 1
        print(cake)
    if cake == 1:
        print(make)
    else:
        return cake
    return make

print('\nbake')
bake(0, 29)                 # >>>  1 and 29 and return 29
bake(1, 'mashed potatoes')  # >>>  mashed potatoes and return 'mashed potatoes


# More Coding Practice

print('\nQ8: Fix the Bug')

# The following snippet of code doesn't work! Figure out what is wrong and fix the bugs.
def both_positive(x, y):
    """Returns True if both x and y are positive."""
    # return x and y > 0  # You can replace this line!
    return x > 0 and y > 0

if __name__ == '__main__':
    print('\nboth_positve')
    assert both_positive(-1, 1) == False
    assert both_positive(1, 1) == True
    print('all passed')

print('\nQ9: Falling Factorial')

def falling(n, k):
    """Compute the falling factorial of n to depth k."""
    result = 1
    while k != 0:
        result *= n
        n -= 1
        k -= 1
    return result

if __name__ == '__main__':
    print('\nfalling')
    assert falling(6, 3) == 120, '6 * 5 * 4'
    assert falling(4, 0) == 1
    assert falling(4, 3) == 24, '4 * 3 * 2'
    assert falling(4, 1) == 4
    print('all passed')


# I want to play a game
print('\nGuessing Game')
