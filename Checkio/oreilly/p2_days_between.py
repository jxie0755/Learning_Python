# You are given two dates as tuples with three numbers - year, month and day.
# 19 April 1982 will be (1982, 4, 19).
# Input: Two dates as tuples of integers.
# Output: The difference between the dates in days as an integer.

from datetime import date

def days_diff(date1, date2):
    D1 = date(date1[0], date1[1], date1[2])
    D2 = date(date2[0], date2[1], date2[2])
    # 可以这种方法表示遍历: date(*date2) - date(*date1)
    time_in_between = abs(D1 - D2)
    return time_in_between.days

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
