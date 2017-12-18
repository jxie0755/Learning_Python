# The bill is represented as an array with information about the calls.
# Help Nicola to calculate the cost for each of Sophia calls.
# Each call is represented as a string with date, time and duration of the call in seconds in the follow format:
# "YYYY-MM-DD hh:mm:ss duration"

# Space-Time Communications Co. has several rules on how to calculate the cost of calls:
#
# First 100 (one hundred) minutes in one day are priced at 1 coin per minute;
# After 100 minutes in one day, each minute costs 2 coins per minute;
# All calls are rounded up to the nearest minute. For example 59 sec ≈ 1 min, 61 sec ≈ 2 min;
# Calls count on the day when they began. For example if a call was started 2014-01-01 23:59:59, then it counted to 2014-01-01;

# Input: Information about calls as a tuple of strings.
# Output: The total cost as an integer.

import itertools
def total_cost(calls):
    # create dataset as a list of dictionary for groupby
    dataset = []
    for i in calls:
        temp = {'date': i[0:10], 'minutes': i[20:]}
        dataset.append(temp)
    # sort first to avoid accidents
    dataset.sort(key=lambda x:x['date'])
    # grouby 'date'
    lstg = itertools.groupby(dataset, key=lambda x: x['date'])

    def dayprice(x):
        """"calculate the price by 1 day"""
        minutes = list(map(lambda y:int(y['minutes']), x))
        billable = []
        for i in minutes:
            if i % 60 != 0:
                minutecount = i // 60 + 1
            else:
                minutecount = i // 60
            billable.append(minutecount)
        if sum(billable) > 100:
            return 100 + (sum(billable) - 100) * 2
        else:
            return sum(billable)

    final = 0
    for k, g in lstg:
        final += dayprice(list(g))

    return final


if __name__ == '__main__':
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"
    print('done')


# print(total_cost(("2014-01-01 01:12:13 181",
#                   "2014-01-02 20:11:10 600",
#                   "2014-01-03 01:12:13 6009",
#                   "2014-01-03 12:13:55 200")))














