# problem 3

def isMyNumber(x):
    if x == 28:
        return 0
    if x < 28:
        return -1
    if x >28:
        return 1

def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number.
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number

    returns: integer, the secret number
    '''
    guess = 1
    while True:
        if isMyNumber(guess) == -1:
            guess += 1
        elif isMyNumber(guess) == 1:
            guess -= 1
        else:
            return guess
            break

print(jumpAndBackpedal(isMyNumber))
