# Calculation of cubic root by enumeration.

target = 9

guess = 0
epsilon = 0.00001
increment = 0.00001

while guess**3 < target:
    guess += 1
if guess**3 == target:
    print("The cubic root of", target, "is", guess)
if guess**3 > target:
    guess = guess - 1

while guess**3 - target > epsilon:
    guess += increment
print("The cubic root of", target, "is very close to", guess)

