age = int(input("What is your age?"))
myage = age + 5

# 1 two lines print
print("I am 5 years older than you")
print("Therefore my age is {0}".format(myage))
# 2 one line command to break to two lines.
print("I am 5 years older than you\nTherefore my age is {0}".format(myage))
# 3 try a different expre ssio
print("I am 5 years older than you, therefore my age is", myage)
print("I am 5 years older than you, therefore my age is " + str(myage))
