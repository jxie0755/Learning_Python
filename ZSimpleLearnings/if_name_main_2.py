import if_name_main_1

# Whatever executable codes in file_1 will run first:
# >>>
# The following codes are run in file_1:
# __name__ is now: if_name_main_1
# f(2)= 4

# the section in file 1 under "if __name__ == "__main__":" will now not be executed
print("The following codes are run in file_2:")
print("__name__ is now:", __name__)
print("f(6)=", if_name_main_1.f(6))
# >>>
# following codes are run in file_2:
# __name__ is now: __main__
# 36
