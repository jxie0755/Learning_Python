import m2t

def m3(x):
    return x**4

print(m3(3))
print(m2t.m2(3))

# 如果m2t中 import m1t
print(m2t.m1t.m1(3))

# 如果m2t中 from m1t import m1
print(m2t.m1(3))


