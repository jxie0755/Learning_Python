# P019 Counting Sundays


# 1 Jan 1900 was a Monday.

# Thirty days has September, April, June and November.
# All the rest have thirty-one
# Saving February alone, Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.

# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


import datetime


def count_weekday_of_monthly_first_day(weekday_code, date1, date2):
    """return how many sundays between date1 and date2

    weekday_code: integer 1-7, 1 for monday, 7 for sunday.
    date1: datetime.date object
    date2: datetime.date object

    return number of sundays in between
    """
    count = 0

    # this will not inlcude examine date2
    while date1 != date2:
        if date1.isoweekday() == weekday_code and date1.day == 1:
            count += 1
        date1 += datetime.timedelta(days=1)

    # this is to include date2, in case of it is the first day of a month.
    if date2.isoweekday() == weekday_code and date2.day == 1:
        count += 1

    return count


if __name__ == "__main__":
    A = datetime.date(1901, 1, 1)
    B = datetime.date(2000, 12, 31)
    print(count_weekday_of_monthly_first_day(7, A, B))
    # >>> 171
    # passed
