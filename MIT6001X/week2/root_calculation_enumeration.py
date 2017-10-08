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


# Calculation of cubic root by enumeration.

target = 28

guess = 0
epsilon = 0.0001
increment = 0.0001
trycount = 0

while guess**3 < target:
    guess += 1
    trycount +=1
if guess**3 == target:
    print("The cubic root of", target, "is", guess)
    print("I tried enumeration", trycount, "times to get this result")
else:
    guess = guess -1
    while target - guess**3 > epsilon:
        guess += increment
        trycount += 1
    guess = guess - increment
    print("The cubic root of", target, "is very close to", guess)
    print("The closest cube I can for this guess is", guess**3)
    print("I tried enumeration", trycount, "times to get this result")