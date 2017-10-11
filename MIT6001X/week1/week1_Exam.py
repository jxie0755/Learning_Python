# Week 1 exam is about strings, iteration, branch, while loop, for loop

# P1
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

s = 'azcbobobegghakl'
vnum = 0
for char in s:
    if char == 'a' or char == 'e'or char == 'i' or char == 'o'or char == 'u':
        vnum += 1
print('Number of vowels:', vnum)

# P2
# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print:
# Number of times bob occurs is: 2

s = 'bobbjobooobobybobobbobobioboo'
print(len(s))
vnum = 0
n = 0
while n <= (len(s) - 2):
    if s[n:n+3] == 'bob':
        vnum += 1
    n += 1
print('Number of times bob occurs is:', vnum)


# P3
# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring.
# For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

s = 'azcbobobegghakl'
n = 0
while n < len(s):
    for m in range(0, n+1):
        target = (s[m:(len(s)-n+m)])
        if target == ''.join(i for i in sorted(target)):
            print('Longest substring in alphabetical order is:', target)
            n = 1 + len(s)  # 先结束while loop
            break   # 再结束for loop,这时候,同时也确保了整个loop就此终结
            # 如果先break for loop,那么n=1+len(s)就永远不会之行,这样就不能有效终止while loop
    else:
        n += 1


s = 'azcbobobegghakl'
n = 0
while n < len(s):
    for m in range(0, n+1):
        target = (s[m:(len(s)-n+m)])
        x = len(target)
        for i in range(0, x - 1):
            if target[i] > target[i + 1]:
                break
        else:
            print('Longest substring in alphabetical order is:', target)
            n = 1 + len(s)
            break
    else:
        n += 1

