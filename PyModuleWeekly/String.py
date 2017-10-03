import string


# capwords - capitalize the first letter in each word. like the method title()
s = 'The quick brown fox jumped over the lazy dog.'
print(s)
print(string.capwords(s))

print()

# string.Template
values = {'var': 'foo'}
t = string.Template("""
Variable:         $var
Escape:           $$
Variable in text: ${var}iable
""")
print('TEMPLATE', t.substitute(values))

s = """
Variable        : %(var)s
Escape          : %%
Variable in text: %(var)siable
"""

print('INTERPOLATION', s % values)

s = """
Variable        : {var}
Escape          : {{}}
Variable in text: {var}iable"""

print('FORMAT', s.format(**values))

print()

values = {'var': 'foo'}

t = string.Template("$var is here but $missing is not provided")

try:
    print('substitute()     :', t.substitute(values))
except KeyError as err:
    print('ERROR:', str(err))

print('safe_substitute():', t.safe_substitute(values))

print()

try:
    with open('1.txt') as f_obj:
        t = f_obj.readlines()
except FileNotFoundError as err:
    print('error:', str(err))
