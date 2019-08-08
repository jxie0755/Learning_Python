# Calculation of the factorial (阶乘)
# n! = n*(n-1)*(n-2)*(n-3)...*1

def factorial(a):
    if a == 1:
        return a
    else:
        return a * factorial(a-1)

print(factorial(5))
print(5*4*3*2*1)