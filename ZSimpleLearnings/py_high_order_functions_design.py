
# Showed by designing a number of function to calculate the square root of a number
# http://composingprograms.com/pages/16-higher-order-functions.html

# This is a high-order function that can be used to keep updating a value until it meets the requirement
# this method uses the update x by calling average(x, a/x), different than binary search method.

def improve(update, close, guess=1):
    while not close(guess):     # keep trying until close returns True
        guess = update(guess)   # a method to update the value so that it can be tested by close again
    return guess                # when it is done, the final guess is the answer
    
def average(x, y):                         # define averaging method as a pre-processing method for update
    return (x + y)/2

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance          # define what is close enough as it will never reach to full equivalence

def sqrt(a):
    def sqrt_update(x):  # if not close enough (x*x not close to a)
        return average(x, a/x)   # this is defined because update can take 1 argument, but we need 2 here to update
    def sqrt_close(x):   # use as the close judgement
        return approx_eq(x * x, a)  # this is called to because update can take 1 argument, but we need 2 here to update
    return improve(sqrt_update, sqrt_close)

print(sqrt(5))



# Simplified version by putting approx_eq inside of sqrt_close and average inside of sqrt_update 

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def sqrt(a):
    def sqrt_update(x):  # if not close enough (x*x not close to a)
        return (x + a/x)/2   # this is called because update can take 1 argument, but we need 2 here to update
    def sqrt_close(x):   # use as the close judgement
        return abs(x*x - a) < 1e-15  # this is called to because update can take 1 argument, but we need 2 here to update
    return improve(sqrt_update, sqrt_close)

print(sqrt(5))
