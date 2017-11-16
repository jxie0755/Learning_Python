from re_test_patterns import find_patterns

# find either 'a' or 'b'
find_patterns('abbaabbba', '[ab]')

# find 'a' followed by 1 or more 'a' or 'b'
find_patterns('abbaabbba', 'a[ab]+')

# find 'a' followed by just 1 'a' or 'b', not greedy'
find_patterns('abbaabbba', 'a[ab]+?')

# output not shown
