for i in range(1, 5):
    print(i)
print("The loop is over")

# 此代码, 将会打印1-4, 但是不会包括5!

for i in range(1, 5):
    print(i)
    if i == 3:
        break
print("The loop is over")

# 由于加入break命令, 导致数到3就结束
