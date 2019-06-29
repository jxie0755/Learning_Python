# This is to show how to find median idx regardless of edd or even number in an array

length = 7
# 0 1 2 3 4 5 6  (len=7, mid_idx = 3)
m1 = (length + 1)// 2 - 1
m2 = (length + 2)// 2 - 1
print(m1, m2) # >>>  3, 3

length = 8
# 0 1 2 3 4 5 6 7 (len=8, mid_idx = 3, 4)
m1 = (length + 1)// 2 - 1
m2 = (length + 2)// 2 - 1
print(m1, m2) # >>>  3, 4


