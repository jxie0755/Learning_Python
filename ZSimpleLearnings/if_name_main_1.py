# when file_1 is imported by another file, all codes in file_1 will be run
# so we make sure file_1 only contains definitions of class and functions, etc.
# BUT sometimes, we write test codes or other codes in file_1, and we don't want them to run after imported to file_2.

def f(x):
    return x**2

print("The following codes are run in file_1:")
print("__name__ is now:", __name__)
# >>> __main__   # codes run in this file shows __main__
print("f(2)=", f(2))  # >>> 4
# especially the test case, if the test case fail, it will impact all
assert(f(4) == 16)  # especially the test case
print()

# >>>
# The following codes are run in file_1:
# __name__ is now: __main__
# f1(2)= 4

# THIS will avoid the codes being executed when this file_1 is imported to another file
if __name__ == "__main__":
    print("this part won't show in file 2:")
    print("f(8)=", f(8))
    assert(f(9) == 81)
# >>>
# this part won't show in file_2
# 64
