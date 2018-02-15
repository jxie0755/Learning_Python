# re_repetition

from re_test_patterns import find_patterns

# 特殊符号简化寻找目标
# 接陈以上函数find_patterns()

# find 'a' followed by zero or more 'b'
find_patterns('abbaabbba', 'ab*')

# find 'a followed by one or more b'
find_patterns('abbaabbba', 'ab+')

# find 'a' followed by zero or one 'b'
find_patterns('abbaabbba', 'ab?')

# find 'a' followed by three 'b'
find_patterns('abbaabbba', 'ab{3}')

# find 'a' followed by two to three 'b'
find_patterns('abbaabbba', 'ab{2,3}')

# find 'a' or 'b', equal to [ab]
find_patterns('asdfjcdbsd', 'a|b')

# find 'ba' at the end
find_patterns('abbaabbba', 'ba$')

# output not shown
