import re

# Precompile the patterns

# 同时搜索多个pattern
regexes = [re.compile(p) for p in ['this', 'that']]
text = 'Does this text match the pattern?'
# >>> regexes is [re.compile('this'), re.compile('that')]

print('Text: {!r}\n'.format(text))

for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern), end=' ')

    if regex.search(text):
        print('match!')
    else:
        print('no match')


target = re.compile('match')
text = 'Does this text match the pattern?'
# 这个命令不是一个boolean output
print(target.search(text))  # >>> <_sre.SRE_Match object; span=(15, 20), match='match'>

if target.search(text):
    print('True')  # >>> True

# 结合前两者
print()
# Precompile the patterns
regex = re.compile('this')
text = 'Does this text match the pattern?'
print(f'Text: {text!r}')
if regex.search(text):
    match = re.search(regex, text)
    s = match.start()
    e = match.end()
    print('you can find it in ' + f'text[{s}:{e}]')

else:
    print('no match')
