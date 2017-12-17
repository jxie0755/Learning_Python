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

