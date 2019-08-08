# calculation of exponential

# iteration version
def iterPower(base, exp):
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result

print(iterPower(4, 3))

# recursion version
def recurPower(base, exp):
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp-1)
print(recurPower(4, 3))
