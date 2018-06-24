# This is a useful function from Checkio/mine/p5_flatten_a_list.py
# Function is to flatten a list that contains list, and nested to unlimited levels.

def flat_list(nested_list):
    flattened_list = []
    for i in nested_list:
        if type(i) == list:
            flattened_list += flat_list(i)
        else:
            flattened_list.append(i)
    return flattened_list

# Version 2, 新建一个frame,然后用helper function
def flat_list(nested_list):
    result = []
    def helper(nested_list):
        for i in nested_list:
            if type(i) == list:
                helper(i)
            else:
                result.append(i)
    helper(nested_list)
    return result

if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
