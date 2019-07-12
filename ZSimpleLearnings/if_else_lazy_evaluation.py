# This is to learn the lazy evaluation effect of if/else condition in python

def lucky(n):
    if n < 7:      # if the condition is False, won't evaluate the rest prt
        return 1 / 0     # bypassed
    elif n == 13:
        return "A" + 5
    else:
        print("omg")
lucky(37)  # >>> omg


def uh_oh():
    if 1 / 0 == 5:      # Will always evaluate the condition
        print("really?")

# uh_oh()  # >>> Error