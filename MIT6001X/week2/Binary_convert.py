# this is to convert a binary number to decimal number

import re

while True:
    target = input("please input a binary number:")
    if not re.match("^[0-1]*$", target):
        print("Error! Only digits 0 and 1 allowed!")
        continue
    else:
        break
ans = 0
numlevel = len(target)
for index in range(0, numlevel):
    ans += int(target[numlevel - index - 1]) * 2**index
print(ans)
print(bin(ans))