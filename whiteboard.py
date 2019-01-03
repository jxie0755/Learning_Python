from math import factorial

def combination(n, m):
    return factorial(n) / factorial(m) / factorial(n - m)


# 第5行,第3个数字
print(combination(5-1, 3-1))

