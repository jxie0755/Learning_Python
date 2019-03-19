# eval() function is to convert a variable's value ('string') into a code through using the variable's name

# Example: list.count()
a = [1,2,3,1,2,3,4,1,2,5,6,7]
b = 'count'
target = 2

# regular way
print(a.count(target))  # >>> 3

# use f string to bring variable in, but also use 'count' string to execute the count() function.
print(eval(f'{a}' + '.' + b + f'({target})'))  # >>> 3

# actually, you don't need f-string to bring-in variables.
print(eval('a' + '.' + b + '(target)'))  # >>> 3


# STOF: https://stackoverflow.com/q/47898221/8435726
# BE VERY CAREFUL TO USE EVAL
# TRY NOT TO USE IT AS MUCH AS POSSIBLE!!


# exec() turn a string into a python line of codes
# it is as dangerous as eval() for the same reason

x = 'lst = [i for i in range(4)]'
xx = 'lstx = [i for i in range(4)]'
y = 'lst.append(9)'

exec(x)
print(lst)  # >>> [0, 1, 2, 3]
# lst.append(9)

exec(y)
print(lst)  # >>> [0, 1, 2, 3, 9]

eval(y)  # eval will also work
print(lst)  # >>> [0, 1, 2, 3, 9, 9]


# AVOID USING THIS!!
