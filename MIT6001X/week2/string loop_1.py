# This is to break down the string into single letters and iterate.
# Two way to do it, by index or by just i

s = 'abcdefghijklmn'

for index in range(len(s)):
    if s[index] == 'a' or s[index] == 'i':
        print("There is 'a' or 'i' in this string")

# Easier to understand
for char in s:
    if char == 'a' or char == 'i':
        print("There is  'a' or 'i' in this string")