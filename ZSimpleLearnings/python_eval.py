# eval() function is to convert a string to a piece of codes

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


# https://stackoverflow.com/questions/47898221/should-i-use-f-string-when-writing-with-eval?noredirect=1#comment82763268_47898221
# BE VERY CAREFUL TO USE EVAL
# TRY NOT TO USE IT AS MUCH AS POSSIBLE!!
