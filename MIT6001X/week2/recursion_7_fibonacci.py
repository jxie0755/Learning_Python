# Fibonacci numbers
# new rabbits born by month:
# 0, 1, 2, 3 ,4 ,5, 6 (month)
# 1, 1, 2, 3, 5, 8, 13....(rabbits)
# how many female rabbits in total in any month?
# females(n) = females(n-1)+females(n-2)

# Use recursion to solve this problem
def fibRecur(i):
    """
    Fibonacci function practice

    :param i: month number
    :return: returns the number of female at month i
    """
    if i == 0 or i == 1:
        return 1
    else:
        return fibRecur(i-1) + fibRecur(i-2)

print(fibRecur(6))


def sumFemale(i):
    """
    Fibonacci function practice

    :param i: month number
    :return: the total number of female rabbits after month i
    """
    sumFem = 0
    while i >= 0:
        sumFem += fibRecur(i)
        i -= 1
    return sumFem

print(sumFemale(6))
