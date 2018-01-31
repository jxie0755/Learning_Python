# a series of fucntions to obtain consecutive substring or subset, work on both types (iterable)
# different ways to get substrings from a long string

# from short to long
def substring_SL(iterable):
    result = []
    for lenth in range(1, len(iterable) + 1):
        for start in range(len(iterable) - lenth + 1):
            result.append(iterable[start:start + lenth])
    return result

if __name__ == '__main__':
    print(substring_SL('abcd'))
    print(substring_SL([1,2,3,4]))
# >>> ['a', 'b', 'c', 'd', 'ab', 'bc', 'cd', 'abc', 'bcd', 'abcd']
# >>> [[1], [2], [3], [4], [1, 2], [2, 3], [3, 4], [1, 2, 3], [2, 3, 4], [1, 2, 3, 4]]


# version 2
def substring_SL2(iterable):
    result = []
    n, m = 0, 0
    index = len(iterable)
    while n < index:
        for m in range(0, index):
            if 1 + m + n <= index:
                result.append(iterable[m:1 + m + n])
        n += 1
    return result

if __name__ == '__main__':
    print(substring_SL2('abcd'))
    print(substring_SL2([1,2,3,4]))
# >>> ['a', 'b', 'c', 'd', 'ab', 'bc', 'cd', 'abc', 'bcd', 'abcd']
# >>> [[1], [2], [3], [4], [1, 2], [2, 3], [3, 4], [1, 2, 3], [2, 3, 4], [1, 2, 3, 4]]


# from long to short
def substring_LS(iterable):
    result = []
    for lenth in range(len(iterable), 0, -1):
        for start in range(len(iterable) - lenth + 1):
            result.append(iterable[start:start + lenth])
    return result

if __name__ == '__main__':
    print(substring_LS('abcd'))
    print(substring_LS([1,2,3,4]))
# >>> ['abcd', 'abc', 'bcd', 'ab', 'bc', 'cd', 'a', 'b', 'c', 'd']
# >>> [[1, 2, 3, 4], [1, 2, 3], [2, 3, 4], [1, 2], [2, 3], [3, 4], [1], [2], [3], [4]]


# version 2
def substring_LS2(iterable):
    result = []
    n, m = 0, 0
    index = len(iterable)
    while n < index:
        for m in range(0, n + 1):
            result.append(iterable[m:index - n + m])
        n += 1
    return result

if __name__ == '__main__':
    print(substring_LS2('abcd'))
    print(substring_LS2([1,2,3,4]))
# >>> ['abcd', 'abc', 'bcd', 'ab', 'bc', 'cd', 'a', 'b', 'c', 'd']
# >>> [[1, 2, 3, 4], [1, 2, 3], [2, 3, 4], [1, 2], [2, 3], [3, 4], [1], [2], [3], [4]]

# 第三种方式找substring, 新的寻找顺序.
def substring_seq(iterable):
    result = []
    for start in range(len(iterable)):
        for end in range(start+1, len(iterable)+1):
            result.append(iterable[start:end])
    return result

if __name__ == '__main__':
    print(substring_seq('abcd'))
    print(substring_seq([1,2,3,4]))
# >>> ['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd', 'd']
# >>> [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [2], [2, 3], [2, 3, 4], [3], [3, 4], [4]]
