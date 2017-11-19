# sub-string
# different ways to get substrings from a long string

# from short to long
def f(x):
    result = []
    n, m = 0, 0
    word = len(x)
    while n < word:
        for m in range(0, word):
            if 1 + m + n <= word:
                result.append(x[m:1 + m + n])
        else:
            n += 1
    return result

# f('abcd') >>> ['a', 'b', 'c', 'd', 'ab', 'bc', 'cd', 'abc', 'bcd', 'abcd']

# from long to short
def g(x):
    result = []
    n, m = 0, 0
    word = len(x)
    while n < word:
        for m in range(0, n + 1):
            result.append(x[m:word - n + m])
        else:
            n += 1
    return result

# g('abcd') >>> ['abcd', 'abc', 'bcd', 'ab', 'bc', 'cd', 'a', 'b', 'c', 'd']

# 注意f(x)和g(x)不是[::-1]的关系.


