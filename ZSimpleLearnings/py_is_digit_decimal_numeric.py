# investigation of isdigit(), isdecimal(), isnumeric

print()
num = "1"  #unicode
print(num.isdigit())    # True
print(num.isdecimal())  # True
print(num.isnumeric())  # True

print()
num = "１" # 全角
print(num.isdigit())    # True
print(num.isdecimal())  # True
print(num.isnumeric())  # True

print()
num = b"1" # byte
print(num.isdigit())    # True
# num.isdecimal()  # AttributeError 'bytes' object has no attribute 'isdecimal'
# num.isnumeric()  # AttributeError 'bytes' object has no attribute 'isnumeric'

print()
num = "四" # 汉字
print(num.isdigit())    # False
print(num.isdecimal())  # False
print(num.isnumeric())  # True
