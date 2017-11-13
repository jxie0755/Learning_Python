import re

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




