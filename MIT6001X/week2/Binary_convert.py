# this is to convert a binary number to decimal number

target = input("please input a binary number:")
ans = 0
numlevel = len(target)
for index in range(0, numlevel):
    ans += int(target[numlevel - index - 1]) * 2**index
print(ans)

