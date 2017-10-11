s = 'abcdefg'

for i in range(0, 6):
    if s[i] < s[i+1]:
        print('ll')
        continue
print('ok')