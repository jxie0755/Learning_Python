# learn mutable data

# '==' and 'is'
# '==' evaluates the value
# 'is' evaluates the identity
a = [10]
b = [10]
print(a == b) # >>> True
print(a is b) # >>> False


# Beaware of the mutable object as default argument of a function!!!
def f(s=[]):
    s.append(5)
    return len(s)

print(f()) # >>> 1
print(f()) # >>> 2
print(f()) # >>> 3
# it remembers the s has changed, so that s is not the same everytime.
