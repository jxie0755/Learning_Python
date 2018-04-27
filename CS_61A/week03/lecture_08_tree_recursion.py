# CS61A Lecture 08 Tree Recursion

def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

cascade(5)
# >>> 5

cascade(12345)
# 12345
# 1234
# 123
# 12
# 1
# 12
# 123
# 1234
# 12345

