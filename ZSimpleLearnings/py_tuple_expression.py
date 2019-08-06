"""
This is to learn simplified tuple expression in python
Question was bond into a leetcode question:
STOF: https://stackoverflow.com/q/54577667/8435726
"""



# Contrary to popular belief, you don't need parentheses to create tuples:

x = 1,
print(type(x))
# >>> <class "tuple">

# However
print(type(1,))   # Equivalent to type(1)
# >>> <class "int">
# because , can be used as a comma in type()

print(type((1,)))  # or type((1,),)
# >>> <class "tuple">

# This is essentially same idea of:
for x, y in enumerate(["a", "b", "c"]):
    print(x, y)
# >>>
# 0 a
# 1 b
# 2 c
# where we use x, y to represent (x, y) as a tuple
