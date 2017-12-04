# num乘以boolean, 如果是True就还是num,如果是False就直接等于0

# 简单的说就是True = 1, False = 0, 然后计算

a = 123

# 乘法
print(a * True)   # >>> 123
print(a * False)  # >>> 0
print([i * True for i in range(5)])   # >>> [0, 1, 2, 3, 4]
print([i * False for i in range(5)])  # >>> [0, 0, 0, 0, 0]

# 除法 (float result)
print([i / True for i in range(5)])   # >>> [0.0, 1.0, 2.0, 3.0, 4.0]
# print([i / False for i in range(5)])   # >>> ZeroDivisionError: division by zero

# 加法
print([i + True for i in range(5)])   # >>> [1, 2, 3, 4, 5]
print([i + False for i in range(5)])  # >>> [0, 1, 2, 3, 4]

# 减法
print([i - True for i in range(5)])   # >>> [-1, 0, 1, 2, 3]
print([i - False for i in range(5)])  # >>> [0, 1, 2, 3, 4]

