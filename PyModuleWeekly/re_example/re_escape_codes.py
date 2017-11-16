from re_test_patterns import find_patterns

# find sequence of digits
find_patterns('A prime #1 example! 6666666!', r'\d+')

# find sequence of non-digits
find_patterns('A prime #1 example! 6666666!', r'\D+')

# find sequence of whitespace
find_patterns('A prime #1 example! 6666666!', r'\s+')

# find sequence of non-whitespace
find_patterns('A prime #1 example! 6666666!', r'\S+')

# find alphanumeric characters
find_patterns('A prime #1 example! 6666666!', r'\w+')

# find non-alphanumeric
find_patterns('A prime #1 example! 666666!', r'\W+')

# find 'e' at the end of a word (单词的开头或结尾) 不能搜符号
find_patterns('A prime #1 example!\n 666666!', r'e\b')

# find escape code
find_patterns(r'\d+ \D+ \s+', r'\\.\+')
