import sys
print("python version:")
print(sys.version)
# this is nothing

print("Hello, World.")
print("  from Denis Xie")

print("{name} wrote {book}".format(name="Swaroop", book="A Byte of Python"))


a = 2
a = a * 3
print(a)

a = 2
a *= 4
print(a)

print("{0:.3f}".format(1.0 / 3))
print("{0:_^11}".format("hello"))
print("{0:_^12}".format("hello"))
print("{0:_^13}".format("hello"))

# has to be build in python 3
print("a", end=" ")
print("b", end=" ")
print("c")

print(""'I am 5 years older than you
# sdfsdfsadf
Therefore my age is 55
""')
print("a")
