# when file_1 is imported by another file, all codes in file_1 will be run
# so we make sure file_1 only contains definitions of class and functions, etc.
# BUT sometimes, we write test codes or other codes in file_1, and we don't want them to run after imported to file_2.

def f1(x):
    return x**2

print('The following codes are run in file_1:')
print('__name__ is now:', __name__)
# >>> __main__   # codes run in this file shows __main__
print(f1(2))  # >>> 4
print(f1(4))  # >>> 16
print()

# >>>
# The following codes are run in file_1:
# __name__ is now: __main__
# 4
# 16

# THIS will avoid the codes being executed when this file_1 is imported to another file
if __name__ == '__main__':
    print("this part won't show in file 2:")
    print(f1(9))
# >>>
# this part won't show in file_2
# 81
