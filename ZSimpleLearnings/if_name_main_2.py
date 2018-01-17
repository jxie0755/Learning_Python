import if_name_main_1

# Whatever executable codes in file_1 will run first:
# >>>
# The following codes are run in file_1:
# __name__ is now: if_name_main_1
# 4
# 16


print('The following codes are run in file_2:')
print('__name__ is now', __name__)
print(if_name_main_1.f1(6))
# >>>
# following codes are run in file_2:
# __name__ is now __main__
# 36


# the section in file 1 under "if __name__ == '__main__':" will now not be executed


