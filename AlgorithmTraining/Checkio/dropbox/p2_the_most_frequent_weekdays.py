"""
You are given a year as integer (e. g. 2001).
You should return the most frequent day(s) of the week in that year.
The result has to be a list of days sorted by the order of days in week (e. g. ["Monday", "Tuesday"]). Week starts with Monday.

Input: Year as an int.
Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday).
"""


import datetime


def most_frequent_days(year):
    # get a dictionary coorelates the day number to weekday name:
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekdict = dict(zip(range(1, 8), weekdays))

    # get days of this year:
    start, secondday, end = datetime.date(year, 1, 1), datetime.date(year, 1, 2), datetime.date(year + 1, 1, 1)
    yeardays = (end - start).days

    # get the first day of week of this year:
    if yeardays % 7 == 1:
        return [weekdict[start.isoweekday()]]
    elif yeardays % 7 == 2:
        temp = sorted([start.isoweekday(), secondday.isoweekday()])
        return [weekdict[temp[0]], weekdict[temp[1]]]


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) == ["Friday"], "1st example"
    assert most_frequent_days(1152) == ["Tuesday", "Wednesday"], "2nd example"
    assert most_frequent_days(56) == ["Saturday", "Sunday"], "3rd example"
    assert most_frequent_days(2909) == ["Tuesday"], "4th example"
