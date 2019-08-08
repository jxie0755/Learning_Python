"""
your code should be shorter than 140 characters (with whitespaces).
Input data: A nested list with integers.
Output data: The one-dimensional list with integers.
"""

def flat_list(a):
    t = []
    for i in a:
        if type(i) == list:
            t = t + flat_list(i)
        else:
            t.append(i)
    return t

if __name__ == "__main__":
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print("Done! Check it")
