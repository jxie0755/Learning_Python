def print_max(x, y):
    ""'Prints the maximum of two numbers.

Two two values must be integers.\n""'
    x = int(x)
    y = int(y)

    if x > y:
        print(x, "is maxium")
    else:
        print(y, "is maximum")

# 直接输出print就是出结果不附带解释
print_max(3, 5)

# 这句就是打印这个函数的介绍出来
print(print_max.__doc__)

# 这句就是打印这个函数的help，相当于是打印解释，但是内容更全
help(print_max)
