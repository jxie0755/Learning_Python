# sub-string
# different ways to get substrings from a long string

# from short to long
def f(x):
    result = []
    n, m = 0, 0
    index = len(x)
    while n < index:
        for m in range(0, index):
            if 1 + m + n <= index:
                result.append(x[m:1 + m + n])
        else:
            n += 1
    return result

print(f('abcd'))
# f('abcd') >>> ['a', 'b', 'c', 'd', 'ab', 'bc', 'cd', 'abc', 'bcd', 'abcd']

# from long to short
def g(x):
    result = []
    n, m = 0, 0
    index = len(x)
    while n < index:
        for m in range(0, n + 1):
            result.append(x[m:index - n + m])
        else:
            n += 1
    return result

print(g('abcd'))
# g('abcd') >>> ['abcd', 'abc', 'bcd', 'ab', 'bc', 'cd', 'a', 'b', 'c', 'd']

# 注意f(x)和g(x)不是[::-1]的关系.


# 第三种方式找substring, 新的寻找顺序.
def h(x):
    index = len(x)
    result = []
    for i in range(index):
        for j in range(i+1,index+1):
            result.append(x[i:j])
    return result

print(h('abcd'))
# (h('abcd')) >>> ['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd', 'd']