# Concatenation and method extend

L1 = [2, 1, 3]
L2 = [4, 5, 6]
L3 = L1 + L2
print(L3)

L3.extend((7, 8))
L3.extend(["X", "Y"])
L3.extend({"a": 1, "b": 2})  # does not have to be a list, a tuple is also ok.

print(L3)

# del and remove
L4 = [1, 2, 3, 1, 2, 3, 4, 5]

del(L4[1])    # del an item in the list
L4.remove(1)  # remove a value in the list(only the first one occured
print(L4)
