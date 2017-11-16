from re_test_patterns import find_patterns

# The carat (^) means to look for characters that are not in the set following the carat.

# find sequences without '-', '.' or 'space'
find_patterns('This is some text -- with punctuation.', '[^-. ]+')
# 去掉+号,会找到所有不是在括号内的字符的单字符

# output not shown
