"""
You are given an array with positive numbers and a number N.
You should find the N-th power of the element in the array with the index N.
 If N is outside of the array, then return -1.

Input: Two arguments. An array as a list of integers and a number as a integer.
Output: The result as an integer.
"""

def index_power(array, n):
    try:
        return array[n] ** n
    except:
        return -1

        # return array[n]**n if len(array) > n else -1


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
