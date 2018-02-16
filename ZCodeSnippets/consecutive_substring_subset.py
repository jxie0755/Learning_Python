# a series of fucntions to obtain consecutive substring or subset, work on both types (iterable)
# different ways to get substrings from a long string
# all brutal force methods: O(n^2), more specifically: O(1/2*n^2 + 1/2*n)


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
    # >>> ['a', 'b', 'c', 'd', 'ab', 'bc', 'cd', 'abc', 'bcd', 'abcd']
    print(substring_SL([1,2,3,4]))
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
    # >>> ['abcd', 'abc', 'bcd', 'ab', 'bc', 'cd', 'a', 'b', 'c', 'd']
    print(substring_LS([1,2,3,4]))
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
    # >>> ['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd', 'd']
    print(substring_seq([1,2,3,4]))
    # >>> [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [2], [2, 3], [2, 3, 4], [3], [3, 4], [4]]


# 第四种方式,寻找中心,然后向两边发散,(从palindrome algorithm中获得)
def substring_C(iterable):
    result = []
    # this part assigns the moving of the center, and define the two sides from it
    for i in range(len(iterable)):
        for j in range(2):
            left =i
            right = left + 1
            # this part expand from the center to get all the substrings that share the same center point
            while left >= 0 and right < len(iterable):
                result.append(iterable[left:right+1])
                left -= 1
                right += 1
    return result

if __name__ == '__main__':
    print(substring_C('abcd'))
    # >>> ['a', 'ab', 'b', 'abc', 'bc', 'abcd', 'c', 'bcd', 'cd', 'd']
    print(substring_C([1,2,3,4]))
    # >>> [[1], [1, 2], [2], [1, 2, 3], [2, 3], [1, 2, 3, 4], [3], [2, 3, 4], [3, 4], [4]]

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

            
def gen_substring_C(iterable):
    for i in range(len(iterable)):
        for j in range(2):
            left =i
            right = left + j  
            while left >= 0 and right < len(iterable):
                yield iterable[left:right+1]
                left -= 1
                right += 1

