# bisection search
# narrow down to find sqrt much faster than numeration
# square root of a target

x = 4
epsilon = 0.001
numGuess = 0

# set range (if 0 < x < 1, then low = x, high = 1).
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
    guess = (high + low) / 2  # 这一行代码很关键,必须在循环中重新定义guess,否则while loop不会对guess做出变动
print("It took me", numGuess, "times to find the answer")
print(guess, "is the sqrt of", x, "the square of", guess, "is", guess**2)

print()

# cube root of a target

x = 27
epsilon = 0.001
numGuess = 0

# set range
low = 1.0
high = x
guess = (high + low) / 2

while abs(guess**3 - x) >= epsilon:
    print('low =', str(low), 'high=', high, 'guess=', guess)
    numGuess += 1
    if guess**3 < x:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2
print("It took me", numGuess, "times to find the answer")
print(guess, "is the sqrt of", x, "the square of", guess, "is", guess**3)
