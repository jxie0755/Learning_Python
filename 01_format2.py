age = int(input("What is your age?"))
myage = age + 5

# two lines print
print("I am 5 years older than you")
print("Therefore my age is {0}".format(myage))

# one line command to break to two lines.
print("I am 5 years older than you\nTherefore my age is {0}".format(myage))

# try a different expression
age = int(input("What is your age?"))
myage = age + 5
print("I am 5 years older than you, therefore my age is", myage)
print("I am 5 years older than you, therefore my age is " + str(myage))
