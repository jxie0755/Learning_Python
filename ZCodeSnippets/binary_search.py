# Learn Binary search


# 二分法的错误方式 (移动中值)
def binsearch_x(lst, target):
    """
    Args:
        lst: a sorted lst
        target: target value
    Returns: index of target if found, -1 if not found
    """
    L, H = 0, len(lst) - 1   # while loop前只定L和H
    M = (L + H) // 2
    current = lst[M]

    if lst[L] == target:
        return L
    elif lst[H] == target:
        return H

    while current != target:            # final case 找到target
        if current < target:
            M = (M + H) // 2
        elif current > target:
            M = (M + L) // 2        # 收缩头尾,注意跳过M,避免重叠
        current = lst[M]
    return M  # 如果找不到, 就会陷入死循环


# 二分法的正确方式 (收缩头尾, 移动头尾)
def binsearch(lst, target):
    """
    Args:
        lst: a sorted lst
        target: target value
    Returns: index of target if found, -1 if not found
    """
    L, H = 0, len(lst) - 1   # while loop前只定L和H
    while L <= H:            # final case L == H, 只管头尾
        M = (L + H) // 2
        current = lst[M]     # 在while loop开头求中值
        if current < target:
            L = M + 1        # 收缩头尾,注意跳过M,避免重叠
        elif current > target:
            H = M - 1        # 收缩头尾,注意跳过M,避免重叠
        else:
            return M
    return -1  # 如果找不到,就会出现L和H数值偏差



if __name__ == '__main__':
    assert binsearch([1,2,4,5,6,7], 3) == -1, 'Cannot find 1'
    assert binsearch([1,2,4,5,6,7], 0) == -1, 'Cannot find 1'
    assert binsearch([1,2,4,5,6,7], 8) == -1, 'Cannot find 1'

    assert binsearch([1,2,4,5,6,7], 1) == 0, 'Test 1'
    assert binsearch([1,2,4,5,6,7], 2) == 1, 'Test 2'
    assert binsearch([1,2,4,5,6,7], 6) == 4, 'Test 3'
    assert binsearch([1,2,4,5,6,7], 7) == 5, 'Test 4'

    print('all passed')

