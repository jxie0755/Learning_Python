# a series of fucntions to obtain consecutive substring or subset, work on both types (iterable)
# different ways to get substrings from a long string
# all brutal force methods: O(n^2), actually O(1/2*n^2 + 1/2*n)


# from short to long
# 先确定长度(从短到长),再确定起始index
def substring_SL(iterable):
    result = []
    for lenth in range(1, len(iterable) + 1):
        for i in range(len(iterable) - lenth + 1):
            result.append(iterable[i:i+lenth])
    return result

if __name__ == '__main__':
    print(substring_SL('abcd'))
    print(substring_SL([1,2,3,4]))
# >>> ['a', 'b', 'c', 'd', 'ab', 'bc', 'cd', 'abc', 'bcd', 'abcd']
# >>> [[1], [2], [3], [4], [1, 2], [2, 3], [3, 4], [1, 2, 3], [2, 3, 4], [1, 2, 3, 4]]


# from long to short
# 仍然是先确定长度(通过-1 step,从长到到短),再确定起始index
def substring_LS(iterable):
    result = []
    for lenth in range(len(iterable), 0, -1):
        for i in range(len(iterable) - lenth + 1):
            result.append(iterable[i:i+lenth])
    return result

if __name__ == '__main__':
    print(substring_LS('abcd'))
    print(substring_LS([1,2,3,4]))
# >>> ['abcd', 'abc', 'bcd', 'ab', 'bc', 'cd', 'a', 'b', 'c', 'd']
# >>> [[1, 2, 3, 4], [1, 2, 3], [2, 3, 4], [1, 2], [2, 3], [3, 4], [1], [2], [3], [4]]


# 第三种方式找substring, 新的寻找顺序.
# 交换loop的顺序,先确定起始index,再变化长度
def substring_seq(iterable):
    result = []
    for i in range(len(iterable)):
        for lenth in range(1, len(iterable) - i + 1):
            result.append(iterable[i:i+lenth])
    return result

if __name__ == '__main__':
    print(substring_seq('abcd'))
    print(substring_seq([1,2,3,4]))
# >>> ['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd', 'd']
# >>> [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [2], [2, 3], [2, 3, 4], [3], [3, 4], [4]]


# generator versions of above
def gen_substring_SL(iterable):
    for lenth in range(1, len(iterable) + 1):
        for i in range(len(iterable) - lenth + 1):
            yield iterable[i:i+lenth]

   
def gen_substring_LS(iterable):
    for lenth in range(len(iterable), 0, -1):
        for i in range(len(iterable) - lenth + 1):
            yield iterable[i:i+lenth]


def gen_substrings(iterable):
    for i in range(len(iterable)):
        for lenth in range(1, len(iterable) - i + 1):
            yield iterable[i:i+lenth]


