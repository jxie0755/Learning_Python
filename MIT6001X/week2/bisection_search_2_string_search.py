# Use bisection search to find whether a character is in a string.

# This is the iteration version
def isIn(char, aStr):
    ""'
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    ""'
    sorted_string = "".join(sorted(aStr))
    sorted_string = sorted_string.lstrip()

    index = len(sorted_string)
    low = 0
    high = index - 1
    guess_index = (high + low) // 2
    guess = sorted_string[guess_index]

    if char < sorted_string[low] or char > sorted_string[high]:
        return False
    while True:
        print("low =", str(low), "high=", high, "guess index=", guess_index, "guess=", guess, )
        if guess == char:
            return True
        elif high - low == 1:
            return False
        elif guess > char:
            high = guess_index
        elif guess < char:
            low = guess_index
        guess_index = (high + low) // 2
        guess = sorted_string[guess_index]
    else:
        return False

# Recursion version
def isIn2(char, aStr):
    ""'
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    ""'
    sorted_string = "".join(sorted(aStr))
    sorted_string = sorted_string.lstrip()

    index = len(sorted_string)
    low = 0
    high = index
    guess_index = (high + low) // 2
    if index == 0:
        return False
    guess = sorted_string[guess_index]
    if index <= 1:
        return char == sorted_string[0]
    elif char == guess:
        return True
    elif char < guess:
        return isIn2(char, sorted_string[low:guess_index])
    else:
        return isIn2(char, sorted_string[guess_index+1:high])


# suggested version
def isIn3(char, aStr):
    mid = len(aStr) // 2
    if not aStr:
        return False
    elif char < aStr[mid]:
        return isIn3(char, aStr[:mid])
    elif char > aStr[mid]:
        return isIn3(char, aStr[mid+1:])
    else:
        return True
