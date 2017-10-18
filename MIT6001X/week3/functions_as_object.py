# apply a function to each item in a list

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

L = [1, -2., 3.4]
applyToEach(L, abs)
print(L)

applyToEach(L, int)
print(L)

print()
# apply a list of function to an argument
def applyFuns(L, x):
    for f in L:
        print(f(x))

L = [abs, int]
applyFuns(L, -4.2)

