"""
A median is a numerical value separating the upper half of a sorted array of numbers from the lower half.
In a list where there are an odd number of entities, the median is the number found in the middle of the array.
If the array contains an even number of entities, then there is no single middle value,
instead the median becomes the average of the two numbers found in the middle.
Input: An array as a list of integers.
Output: The median as a float or an integer.
"""

def checkio(data):
    data = sorted(data)
    length = len(data)
    if len(data) % 2 != 0:
        return data[length//2]
    else:
        return (data[length//2] + data[length//2 - 1]) / 2

if __name__ == "__main__":
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")
