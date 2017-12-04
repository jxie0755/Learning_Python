# num乘以boolean, 如果是True就还是num,如果是False就直接等于0

a = 123
print(a * True)   # >>> 123
print(a * False)  # >>> 0


print([i * True for i in range(5)])   # >>> [0, 1, 2, 3, 4]
print([i * False for i in range(5)])  # >>> [0, 0, 0, 0, 0]

