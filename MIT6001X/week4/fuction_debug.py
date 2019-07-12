def isPal(x):
    assert type(x) == list
    temp = x  # should be x[:]
    temp.reverse  # should be reverse()
    print("x is", x)
    print("temp is", temp)
    if temp == x:
        return True
    else:
        return False

msg = [1, 2, 3]
print(isPal(msg))


def silly(n):
    result = []
    for i in range(n):
        # result = [] should be outside of the loop
        elem = input("Enter element: ")
        result.append(elem)
    if isPal(result):
        print("Yes")
    else:
        print("No")

silly(2)
