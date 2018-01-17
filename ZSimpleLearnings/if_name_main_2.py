import if_name_main_1

print('In file 2 we only test one function:')

print(if_name_main_1.f1(6))
# >>>
# In file 1 we have two functions run:
# 4
# 16
# In file 2 we only test one function:
# 36

if __name__ == '__main__':
    print(if_name_main_1.f1(7))
# >>>
# 49   # this only use the functions in file1 and run it in file 2
