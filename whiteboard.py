s = 'abcd'
print(s[1:2])

for j in range(len(s), 0, -1):
    for i in range(0, len(s)-j+1):
        print(s[i:i+j])