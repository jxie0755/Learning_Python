# Calculation of square root by enumeration.

target = 26

guess = 0
epsilon = 0.001
numGuess = 0

while guess**2 < target:
    guess += 1
    numGuess +=0
if guess**2 == target:
    print("I tried enumeration", numGuess, "times to get this result")
    print("The cube root of", target, "is", guess)
else:
    while True:
        guess = (guess + target / guess) / 2
        numGuess += 1
        if guess**2 - target < epsilon:
            print("I tried enumeration", numGuess, "times to get this result")
            print("The square root of", target, "is very close to", guess)
            break


print()
# Calculation of cube root by enumeration.

target = 28

guess = 0
epsilon = 0.0001
increment = 0.0001
numGuess = 0

while guess**3 < target:
    guess += 1
    numGuess +=1
if guess**3 == target:
    print("The cube root of", target, "is", guess)
    print("I tried enumeration", numGuess, "times to get this result")
else:
    guess = guess -1
    while target - guess**3 > epsilon:
        guess += increment
        numGuess += 1
    guess = guess - increment
    print("The cube root of", target, "is very close to", guess)
    print("The closest cube I can for this guess is", guess**3)
    print("I tried enumeration", numGuess, "times to get this result")