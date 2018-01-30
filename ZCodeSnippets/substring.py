# sub-string
# different ways to get substrings from a long string

# from short to long
def substring_SL(s):
    result = []
    for lenth in range(1, len(s) + 1):
        for start in range(len(s) - lenth + 1):
            result.append(s[start:start + lenth])
    return result

if __name__ == '__main__':
    print(substring_SL('abcd'))
# >>> ['a', 'b', 'c', 'd', 'ab', 'bc', 'cd', 'abc', 'bcd', 'abcd']

# version 2
def substring_SL2(s):
    result = []
    n, m = 0, 0
    index = len(s)
    while n < index:
        for m in range(0, index):
            if 1 + m + n <= index:
                result.append(s[m:1 + m + n])
        n += 1
    return result

if __name__ == '__main__':
    print(substring_SL2('abcd'))
# >>> ['a', 'b', 'c', 'd', 'ab', 'bc', 'cd', 'abc', 'bcd', 'abcd']


# from long to short
def substring_LS(s):
    result = []
    for lenth in range(len(s), 0, -1):
        for start in range(len(s) - lenth + 1):
            result.append(s[start:start + lenth])
    return result

if __name__ == '__main__':
    print(substring_LS('abcd'))
# >>> ['abcd', 'abc', 'bcd', 'ab', 'bc', 'cd', 'a', 'b', 'c', 'd']

# version 2
def substring_LS2(s):
    result = []
    n, m = 0, 0
    index = len(s)
    while n < index:
        for m in range(0, n + 1):
            result.append(s[m:index - n + m])
        n += 1
    return result

if __name__ == '__main__':
    print(substring_LS2('abcd'))
# >>> ['abcd', 'abc', 'bcd', 'ab', 'bc', 'cd', 'a', 'b', 'c', 'd']



# 第三种方式找substring, 新的寻找顺序.
def substring_seq(x):
    result = []
    for start in range(len(x)):
        for end in range(start+1,len(x)+1):
            result.append(x[start:end])
    return result

if __name__ == '__main__':
    print(substring_seq('abcd'))
# >>> ['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd', 'd']
