import re

# Precompile the patterns

# 同时搜索多个pattern
regexes = [re.compile(p) for p in ['this', 'that']]
text = 'Does this text match the pattern?'

print('regexes is', regexes)
# >>> regexes is [re.compile('this'), re.compile('that')]

print('Text: {!r}\n'.format(text))

for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern), end=' ')

    if regex.search(text):
        print('match!')
    else:
        print('no match')
