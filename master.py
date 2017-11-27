# You should only see this in master

d = {'a': "1", 'b': "2", "c": 3}

print(sorted(d.keys())[0])
foo='test1'
bar='test2'
print(f"string, id={foo} ip={bar} a={d['a']} b={d['b']} c={d['c']}")
print(' '.join(str(i[0])+'='+str(i[1]) for i in d.items()))

print(d.items())

a = 123
b = 456
print(f'the value of a is {a}, the value of b is {b}')
