from re_test_patterns import find_patterns

# find word at start of string
find_patterns('This is some text -- with punctuation.', r'^\w+')

# find word at start of string
find_patterns('This is some text -- with punctuation.', r'\A\w+')

# find word near end of string
find_patterns('This is some text -- with punctuation.', r'\w+\S*$')

# find word near end of string
find_patterns('This is some text -- with punctuation.', r'\w+\S*\Z')

# find word containing 't'
find_patterns('This is some text -- with punctuation.', r'\w*t\w*')

# find word with 's' at the start
find_patterns('This is some text -- with punctuation.', r'\bs\w+')

# find word with 's' at the end
find_patterns('This is some text -- with punctuation.', r'\w+s\b')

# find 't' at not start or end of word
find_patterns('This is some text -- with punctuation.', r'\Bt\B')
