# bisection search
# narrow down to find sqrt much faster than numeration

x = 26
epsilon = 0.001
numGuess = 0

# set range
low = 1.0
high = x
guess = (high + low) / 2

while abs(guess**2 - x) >= epsilon:
    print('low =', str(low), 'high=', high, 'guess=', guess)
    numGuess += 1
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2
print("It took me", numGuess, "times to find the answer")
print(guess, "is the sqrt of", x, "the square of", guess, "is", guess**2)