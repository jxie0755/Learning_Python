# Use python string method to split a string

name = 'Denis Xie'
print(name.split())  # >>> ['Denis', 'Xie']

s1 = 'abcXabcXabc'
print(s1.split('X'))  # >>> ['abc', 'abc', 'abc']
print(s1.partition('X'))  # >>> ('abc', 'X', 'abcXabc')  # notice partition will do different work

# but what if the string has no space in between?
s2 = '00100011000001'
print(s2.replace('01', '0 1').replace('10', '1 0').split())  # >>>['00', '1', '000', '11', '00000', '1']  
# add space in between and then split
