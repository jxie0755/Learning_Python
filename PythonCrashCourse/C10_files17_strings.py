# string operation

a = '***a b c d e f g**'
b = a.strip('*')
c = b.split()
d = ' '.join(i for i in c)
e = d.replace(' ', '')
f = e.split('c')  # split命令不但通过c分割,还去掉c
g = ''.join(f)


h = []
for i in g:
    h.append(i)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)