"""Example of slice and copy"""

s = "abcd"
length = len(s)
print(s[:] == s[0:] == s[0:length] == s)  # full length of string
print(s[length:0:-1] == s[::-1])  # "dbc", reverse not the same way
print(s[length::-1] == s[::-1])   # "dbca" full reverser

print(s[0:0] == s[1:1] == s[2:2] == s[3:3] == "")  # zero length
print(s[1:2] == s[1], s[3:4] == s[3])   # single length
print(s[1:2:-1] == s[2:3:-1] == "")  # reverse not the same
print(s[2:1:-1] == s[2], s[3:2:-1] == s[3])  # reverse
print(s[3:1:-1] == s[1:3][::-1])  # False
print(s[3:1:-1] == s[2:4][::-1])  # True

# 记住s[x:y:z]从s[x]开始,长度为y-x的substring
# 若 y - x == 0   则 ""
# 若 y - x == 1   则 s[x]
# 若 y - x == -1  则 s[x]
# 若 y - x > 1    则 正向
# 若 y - x < -1   则 方向


t = [1, 2, 3]
print(t[1:10])  # The slice can go over it's own index
# >>>
# [2, 3]
