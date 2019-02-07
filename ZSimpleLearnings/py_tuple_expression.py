# This is to learn simplified tuple expression in python
# Question was bond into a leetcode question:
# https://stackoverflow.com/questions/54577667/cannot-understand-the-critical-comma-in-this-function?noredirect=1#comment95953021_54577667



# Contrary to popular belief, you don't need parentheses to create tuples:

x = 1,
print(type(x))
# >>> <class 'tuple'>

# However
print(type(1,))   # Equivalent to type(1)
# >>> <class 'int'>
# because , can be used as a comma in type()

print(type((1,)))  # or type((1,),)
# >>> <class 'tuple'>
