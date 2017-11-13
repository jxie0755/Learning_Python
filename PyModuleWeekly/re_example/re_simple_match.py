import re

pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print(match.re.pattern)  # >>> 'this'
print(match.string)  # >>> 'Does this text match the pattern?'
print(match.start())  # >>> 5 --- means starting from text[5]
print(match.end())    # >>> 9 --- means ends at text [9]
print(text[s:e])




