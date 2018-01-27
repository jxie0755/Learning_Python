# sub-string
# different ways to get substrings from a long string

# from short to long
def sub_short_long(x):
    result = []
    n, m = 0, 0
    index = len(x)
    while n < index:
        for m in range(0, index):
            if 1 + m + n <= index:
                result.append(x[m:1 + m + n])
        n += 1
    return result

if __name__ == '__main__':
    print(sub_short_long('abcd'))
# >>> ['a', 'b', 'c', 'd', 'ab', 'bc', 'cd', 'abc', 'bcd', 'abcd']

# version 2
def sub_short_long2(x):
    result = []
    for lenth in range(1, len(x) + 1):
        for start in range(len(x) - lenth + 1):
            result.append(x[start:start + lenth])
    return result

if __name__ == '__main__':
    print(sub_short_long2('abcd'))
# >>> ['a', 'b', 'c', 'd', 'ab', 'bc', 'cd', 'abc', 'bcd', 'abcd']


# from long to short
def sub_long_short(x):
    result = []
    n, m = 0, 0
    index = len(x)
    while n < index:
        for m in range(0, n + 1):
            result.append(x[m:index - n + m])
        n += 1
    return result

if __name__ == '__main__':
    print(sub_long_short('abcd'))
# >>> ['abcd', 'abc', 'bcd', 'ab', 'bc', 'cd', 'a', 'b', 'c', 'd']

# version 2
def sub_long_short2(x):
    result = []
    for lenth in range(len(x), 0, -1):
        for start in range(len(x) - lenth + 1):
            result.append(x[start:start + lenth])
    return result

if __name__ == '__main__':
    print(sub_long_short2('abcd'))
# >>> ['abcd', 'abc', 'bcd', 'ab', 'bc', 'cd', 'a', 'b', 'c', 'd']

# 第三种方式找substring, 新的寻找顺序.
def sub_new(x):
    result = []
    for start in range(len(x)):
        for end in range(start+1,len(x)+1):
            result.append(x[start:end])
    return result

if __name__ == '__main__':
    print(sub_new('abcd'))
# >>> ['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd', 'd']