# CS61A Lecture 27 Interpreters
# https://www.youtube.com/watch?v=1hGO8KOELQk&list=PL6BsET-8jgYWkNhlFFR3S-110mYMrIBsM&vq=hd1080


# Structure of the interpreter
# Use eval()
# then apply
# This is a recursive call

# To evaluate nested list (a (b, c (d)))

# there are special forms:
# if condition to skip part of evaluatting
# quote for (' a b c) to skip evaluating
# lambda condition to evaluate a function (done by a python Class to handle)
# define expression is essentially attach the function name to a lambda function

# Need to pay attention to the env (frame, i.e: global)
