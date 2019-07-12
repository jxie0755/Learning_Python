# Learn some simple principle of immutable data, tuple

t = (1,2,3)  # immutable
# no slice
t = 1,2,3
print(t)  # without bracket, it is automatic tuple

print(type(()))
# >>> <class "tuple">
# empty bracket is also considered as tuple

# immutable
d = {(1,2): 3}  # use tuple as dictionary key
# when used as a key, it can not contain mutable data as well
# d = {(1,[2,3]): 3}
# # >>> TypeError: unhashable type: "list"

# But you can change the mutable data inside of a tuple
t = (1,2, [3,4])
t[2][0] = 99
print(t)
# >>> (1, 2, [99, 4])
# that is why it is not allowed to be used as a key
