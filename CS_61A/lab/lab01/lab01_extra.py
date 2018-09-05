# Optional Questions
print('\nOptional Questions')

# Q6 Truthiness What Would Python Display?
print('\nQ6: WWPD: Truthiness')
# python3 ok -q truthiness -u
if __name__ == '__main__':
    print('answers hidden')
    # print(0 or True)                   # >>> True
    # print(not '' or not 0 and False)   # >>> True # 注意运算优先级
    # print(13 and False)                # >>> False
    # print(False or 1)           # >>> True but actually show the value 1
    # # print('' or 1 and 1/0)      # >>> Error
    # print(not 0 and 12 or 0)    # >>> True but actually show the value 12


# Q7 What if? What Would Python Display?
print('\nQ7: WWPD: What If?')
# python3 ok -q what_if -u
if __name__ == '__main__':
    print('answers hidden')
    # def xk(c, d):
    #     if c == 4:
    #         return 6
    #     elif d >= 4:
    #         return 6 + 7 + c
    #     else:
    #         return 25

    # print(xk(10, 10))  # >>> 23
    # print(xk(10, 6))   # >>> 23
    # print(xk(4, 6))    # >>> 6
    # print(xk(0, 0))    # >>> 25

    # def how_big(x):
    #     if x > 10:
    #         print('huge')
    #     elif x > 5:
    #         return 'big'
    #     elif x > 0:
    #         print('small')
    #     else:
    #         print("nothin'")

    # how_big(7)   # >>> return 'big'  # terminal will still show the return as the actuall string
    # how_big(12)  # >>> huge   # when print, it will ingore the "'"
    # how_big(1)   # >>> small
    # how_big(-1)  # >>> nothin'

    # def so_big(x):
    #     if x > 10:
    #         print('huge')
    #     if x > 5:
    #         return 'big'
    #     if x > 0:
    #         print('small')
    #     print("nothin'")

    # so_big(7)   # >>> return 'big'
    # so_big(12)  # >>> huge and return 'big'
    # so_big(1)   # >>> small and nothin'

    # def ab(c, d):
    #     if c > 5:
    #         print(c)
    #     elif c > 7:
    #         print(d)
    #     print('foo')

    # print('\nab')
    # ab(10, 20)  # >>> 10 and foo

    # def bake(cake, make):
    #     if cake == 0:
    #         cake = cake + 1
    #         print(cake)
    #     if cake == 1:
    #         print(make)
    #     else:
    #         return cake
    #     return make

    # print('\nbake')
    # bake(0, 29)                 # >>>  1 and 29 and return 29
    # bake(1, 'mashed potatoes')  # >>>  mashed potatoes and return 'mashed potatoes


# More Coding Practice

print('\nQ8: Fix the Bug')

# The following snippet of code doesn't work! Figure out what is wrong and fix the bugs.
def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    # return x and y > 0  # You can replace this line!
    return x > 0 and y > 0

# python3 ok -q both_positive
print('passed')


print('\nQ9: Falling Factorial')

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    result = 1
    while k != 0:
        result *= n
        n -= 1
        k -= 1
    return result

# python3 ok -q falling
print('passed')

# I want to play a game
print('\nGuessing Game')


from random import randint

LOWER = 1
UPPER = 10

def guess_random():
    """Guess randomly and return the number of guesses."""
    prompt_for_number(LOWER, UPPER)   # asks the user to choose a number
    num_guesses, correct = 0, False
    while not correct:
        guess = randint(LOWER, UPPER) # randomly guess
        correct = is_correct(guess)   # ask user if guess is correct
        num_guesses = num_guesses + 1
    return num_guesses

def guess_linear():
    """Guess in increasing order and return the number of guesses."""
    prompt_for_number(LOWER, UPPER)
    num_guesses = 1
    guess = LOWER
    while not is_correct(guess):
        guess += 1
        num_guesses += 1
    return num_guesses

def guess_binary():
    """Return the number of attempted guesses. Implement a faster search
    algorithm that asks the user whether a guess is less than or greater than
    the correct number.

    Hint: If you know the guess is greater than the correct number, then your
    algorithm doesn't need to try numbers that are greater than guess.
    """
    prompt_for_number(LOWER, UPPER)
    num_guesses = 1
    lower, upper = LOWER, UPPER
    guess = (lower + upper) // 2
    while not is_correct(guess):
        if is_too_high(guess):
            upper = guess - 1
        elif not is_too_high(guess):
            lower = guess + 1
        guess = (lower + upper) // 2
        num_guesses += 1
    return num_guesses

# Receive user input. You do not need to understand the code below this line.

def prompt_for_number(lower, upper):
    """Prompt the user for a number between lower and upper. Return None."""
    is_valid_number = False
    while not is_valid_number:
        # You don't need to understand the following two lines.
        number = input('Pick an integer between {0} and {1} (inclusive) for me to guess: '.format(lower, upper))
        number = int(number)
        if lower <= number <= upper:
            is_valid_number = True

def is_correct(guess):
    """Ask the user if a guess is correct and return whether they respond y."""
    return is_yes('Is {0} your number? [y/n] '.format(guess))

def is_too_high(guess):
    """Ask the user if a guess is too high and return whether they say yes."""
    return is_yes('Is {0} too high? [y/n] '.format(guess))

def is_yes(prompt):
    """Ask the user a yes or no question and return whether they say yes."""
    while True: # This while statement will loop until a "return" is reached.
        yes_no = input(prompt).strip()
        if yes_no == 'y':
            return True
        elif yes_no == 'n':
            return False
        print('Please type y or n and press return/enter')
