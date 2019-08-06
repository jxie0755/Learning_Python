"""
You are given a positive integer.
Your function should calculate the product of the digits excluding any zeroes.

Input: A positive integer.
Output: The product of the digits as an integer.
"""

def checkio(number):
    from functools import reduce
    number = "".join(filter(lambda x: not x == "0", str(number)))
    def mult(x, y):
        return int(x) * int(y)
    return int(reduce(mult, number))

if __name__ == "__main__":
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
