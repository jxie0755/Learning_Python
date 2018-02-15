# re_repetition_non_greedy
# When processing a repetition instruction, re will usually consume as much of the input as possible while matching the pattern.
# Greediness can be turned off by following the repetition instruction with '?'

from re_test_patterns import find_patterns

# find 'a' followed by zero 'b', equal to 'a'
find_patterns('abbaabbba', 'ab*?')

# find 'a' followed by one 'b', equal to 'ab'
find_patterns('abbaabbba', 'ab+?')

# find 'a' followed by zero 'b', equal to just 'a'
find_patterns('abbaabbba', 'ab??')

# find 'a' followed by three 'b', equal to 'ab{3}'
find_patterns('abbaabbba', 'ab{3}?')

# # find 'a' followed by two 'b', equal to 'ab{2}'
find_patterns('abbaabbba', 'ab{2,3}?')

# output not shown
