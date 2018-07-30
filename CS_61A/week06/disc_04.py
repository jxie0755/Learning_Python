# CS61A Discussion 04 Nonlocals & Mutation


# Nonlocal
def stepper(num):
    def step():
        nonlocal num
        num = num + 1
        return num
    return step

s = stepper(3)
print(s()) # >>> 4
print(s()) # >>> 5
