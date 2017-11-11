s = 'abcdefg'
n = 0
m = 0
word = len(s)
while n < word:
    for m in range(0, n+1):
        print(s[m:word-n+m])
    else:
        n += 1

print()

# find all substring (sub-string)
s = 'abcdefg'
n = 0
m = 0
word = len(s)
while n < word:
    for m in range(0, word):
        if 1+m+n <= word:
            print(s[m:1+m+n])
    else:
        n += 1
