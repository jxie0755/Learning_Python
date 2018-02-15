from re_test_patterns import find_patterns

# find sequences of lowercase letters
find_patterns('This is some text -- with punctuation.', '[a-z]+')

# find sequences of uppercase letters
find_patterns('This is some text -- with punctuation.', '[A-Z]+')

# find sequences of letters of either case
find_patterns('This is some text -- with punctuation.', '[a-zA-Z]+')

# find one uppercase followed by lowercase
find_patterns('This is some text -- with punctuation.', '[A-Z][a-z]+')

# output not shown
