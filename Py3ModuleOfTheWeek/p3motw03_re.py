# https://pymotw.com/3/re/index.html
# additional:
# https://morvanzhou.github.io/tutorials/python-basic/basic/13-10-regular-expression/

import re

# re_simple_match.py
print()
print('**********************************************************')
print('re_simple_match')

# 建立在能够被search的条件
pattern = 'this'
text = 'Does this text match the pattern?'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print(match.re.pattern)  # >>> 'this'
print(match.string)  # >>> 'Does this text match the pattern?'
# 如果无法被search到,以下则报错
print(match.start())  # >>> 5 --- means starting from text[5]
print(match.end())    # >>> 9 --- means ends at text [9]
print(text[s:e])


# re_simple_compiled.py
print()
print('**********************************************************')
print('re_simple_compiled')

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


# re_findall.py
print()
print('**********************************************************')
print('re_findall')

text = 'abbaaabbbbaaaaa'
target = 'ab'
print(re.findall(target, text))
# >>> ['ab', 'ab'], findall生成一个list把全部找到的都放入该list
# 使用keywords来直接表达
print(len(re.findall(pattern='abc', string='abcdabceabcfabc')))
# >>> 用len()来计量找到了几个


# re_finditer.py

text = 'abbaaabbbbaaaaa'
pattern = 'ab'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found {!r} at {:d}:{:d}'.format(
        text[s:e], s, e))


# re_test_patterns.py
print()
print('**********************************************************')
print('re_test_patterns')

# 利用finditer找出所有的match并且返回它们的位置

def find_patterns(text, pattern):
    # Look for each pattern in the text and print the results

    print(f"\nTo Find: {pattern!r}")
    print(f"In:\n{text!r}\n")

    for match in re.finditer(pattern, text):
        s = match.start()
        e = match.end()
        print('Find at', f'text[{s}:{e}]')
        substr = text[s:e]
        n_backslashes = text[:s].count('\\')
        prefix = '.' * (s + n_backslashes)
        print("{}'{}'".format(prefix, substr))

find_patterns('vvabbaaabbbbaaaaa', 'ab')


# re_repetition.py
print()
print('**********************************************************')
print('re_repetition')

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


# re_repetition_non_greedy.py
print()
print('**********************************************************')
print('re_repetition_non_greedy')

# When processing a repetition instruction, re will usually consume as much of the input as possible while matching the pattern.
# Greediness can be turned off by following the repetition instruction with '?'

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


# re_charset.py
print()
print('**********************************************************')
print('re_charset')

# find either 'a' or 'b'
find_patterns('abbaabbba', '[ab]')
# find 'a' followed by 1 or more 'a' or 'b'
find_patterns('abbaabbba', 'a[ab]+')
# find 'a' followed by just 1 'a' or 'b', not greedy'
find_patterns('abbaabbba', 'a[ab]+?')
# output not shown


# re_charset_exclude.py
print()
print('**********************************************************')
print('re_charset_exclude')

# The carat (^) means to look for characters that are not in the set following the carat.
# find sequences without '-', '.' or 'space'
find_patterns('This is some text -- with punctuation.', '[^-. ]+')
# 去掉+号,会找到所有不是在括号内的字符的单字符
# output not shown


# re_charset_ranges.py
print()
print('**********************************************************')
print('re_charset_ranges')

# find sequences of lowercase letters
find_patterns('This is some text -- with punctuation.', '[a-z]+')
# find sequences of uppercase letters
find_patterns('This is some text -- with punctuation.', '[A-Z]+')
# find sequences of letters of either case
find_patterns('This is some text -- with punctuation.', '[a-zA-Z]+')
# find one uppercase followed by lowercase
find_patterns('This is some text -- with punctuation.', '[A-Z][a-z]+')
# output not shown


# re_charset_dot.py
print()
print('**********************************************************')
print('re_charset_dot')

# a followed by any one character
find_patterns('abbaabbba', 'a.')
# b followed by any one character
find_patterns('abbaabbba', 'b.')
# a followed by anything, ending in b
find_patterns('abbaabbba', 'a.*b')
# a followed by anything, ending in b
find_patterns('abbaabbba', 'a.*?b')


# re_escape_codes.py
print()
print('**********************************************************')
print('re_escape_codes')

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


# re_escapte_excaptes.py
print()
print('**********************************************************')
print('re_escapte_excaptes')

# escape code
find_patterns(r'\d+ \D+ \s+', r'\\.\+')


# re_anchoring.py
print()
print('**********************************************************')
print('re_anchoring')

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

# TODO

# re_match.py
print()
print('**********************************************************')
print('re_match')

text = 'This is some text -- with punctuation.'
pattern = 'is'
print('Text   :', text)
print('Pattern:', pattern)
m = re.match(pattern, text)
print('Match  :', m)
s = re.search(pattern, text)
print('Search :', s)


# re_fullmatch.py
print()
print('**********************************************************')
print('re_fullmatch')

text = 'This is some text -- with punctuation.'
pattern = 'is'
print('Text       :', text)
print('Pattern    :', pattern)
m = re.search(pattern, text)
print('Search     :', m)
s = re.fullmatch(pattern, text)
print('Full match :', s)


