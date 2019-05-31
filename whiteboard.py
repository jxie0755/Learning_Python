
lst = []
def foo(x):
    lst.append(x)
    if x == 1:
        return True
    else:
        return False

print(5 and 6 and foo(5) and foo(1))
print(lst)
