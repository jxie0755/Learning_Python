import string


# capwords - capitalize the first letter in each word. like the method title()
s = 'The quick brown fox jumped over the lazy dog.'
print(s)
print(string.capwords(s))

print()

# string.Template
dict1 = {'gg': 'foo'}

t = string.Template(""" 
Variable        : $gg 
Escape          : $$ 
Variable in text: ${gg}iable 
""")

print('TEMPLATE:', t.substitute(dict1))

s = """ 
Variable        : %(gg)s 
Escape          : %% 
Variable in text: %(gg)siable 
"""

print('INTERPOLATION:', s % dict1)

s = """ 
Variable        : {gg} 
Escape          : {{}} 
Variable in text: {gg}iable 
"""

print('FORMAT:', s.format(**dict1))

print()

# 简单实例: 把一个字符串变成Template()的实例, 对于实例使用类的方法substitute,将$开头的变量置换为另一个字符
s = 'hello, $world!'
t = string.Template(s)
print(t.substitute({'world':'nimei'}))

print()

# safe_substitute方法, 万一有些value
# there is no value for missing in the values dictionary, a KeyError is raised by substitute().
# Instead of raising the error, safe_substitute() catches it and leaves the variable expression alone in the text.
values = {'var': 'foo'}

t = string.Template("$var is here but $missing is not provided")

try:
    print('substitute()     :', t.substitute(values))
except KeyError as err:
    print('ERROR:', str(err))

print('safe_substitute():', t.safe_substitute(values))

print()

import inspect
import string

def is_str(value):
    return isinstance(value, str)

for name, value in inspect.getmembers(string, is_str):
    if name.startswith('_'):
        continue
    print('%s=%r\n' % (name, value))
