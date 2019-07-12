x = 2
def say_hello(x):
    print("hello world")

say_hello(x)
say_hello(x)

def print_max(a, b):
    if a > b:
        print(a, "is maximum")
    if a == b:
        print(a, "is equal to", b)
    else:
        print(b, "is maximum")

print_max(3, 4)

x = 5
y = 7
print_max(x, y)
