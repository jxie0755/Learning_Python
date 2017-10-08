# Calculation of square root by enumeration.

target = 6

guess = 0
epsilon = 0.000001

while guess**2 < target:
    guess += 1
if guess**2 == target:
    print("The cubic root of", target, "is", guess)
else:
    while True:
        guess = (guess + target / guess) / 2
        if guess**2 - target < epsilon:
            print("The cubic root of", target, "is very close to", guess)
            break
