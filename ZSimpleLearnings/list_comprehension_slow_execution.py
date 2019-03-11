# List comprehension vs Straightforward for loop
# STOF https://stackoverflow.com/questions/27905965/python-why-is-list-comprehension-slower-than-for-loop

def lcm(X):
    n = 0
    while True:
        n += 1
        for i in range(2,X+1):    # use straightforward for loop
            if n%i!=0:
                break
        else:
            break
    return n

# print(lcm(20))
# >>> takes about ~100 sec

def lcm2(X):
    n = 0
    while True:
        n += 1
        if all(n % i == 0 for i in range(2, X+1)):   # use list comprehension
            return n


# print(lcm2(20))
# >>> takes about ~200 sec


# it is slower because list comprehension creates a generator:
# Generator expressions require a new frame to be created each time you run one, just like a function call. This is relatively expensive.
