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

# this is to convert a decimal number to binary
# 用2辗转相除至结果为1
# 将余数和最后的1从下向上倒序写 就是结果 （逆序）
# 例如302
# 302/2 = 151 余0
# 151/2 = 75 余1
# 75/2 = 37 余1
# 37/2 = 18 余1
# 18/2 = 9 余0
# 9/2 = 4 余1
# 4/2 = 2 余0
# 2/2 = 1 余0
# 故二进制为100101110

import re

while True:
    target = input("please input a decimal number:")
    if not re.match("^[0-9]*$", target):
        print("Error! Only digits 0 and 1 allowed!")
        continue
    else:
        break
int_target = int(target)
biList = []
while True:
    biList.append(int_target % 2)
    int_target = int(int_target / 2)
    if int_target == 1:
        biList.append(int_target % 2)
        break
biList.reverse()
binumber = int(''.join(biList))
print('The binary number of', int(target), "is", binumber)
