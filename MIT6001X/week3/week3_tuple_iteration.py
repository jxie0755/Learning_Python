# an example to show how to iterate a tuple

# this is a function to get data from a tuple that contains a lot of sub-tuples

aTuple = (('a', 1), ('b', 2), ('c', 3), ('d', 4), ('d', 5))


def get_data(atuple):
    nums = ()
    words = ()
    for t in atuple:
        nums = nums + (t[1],) # 注意,这里一定要把t[1]变成一个单元素tuple,只有这样才能合并进入到原tuple
        if t[0] not in words:
            words = words + (t[0],) # 同上
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)


print(get_data(aTuple))
(small, large, words) = get_data(aTuple)
print(small)
print(large)
print(words)
