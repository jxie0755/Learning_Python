import string

# a string contains all letters
str = string.ascii_lowercase
print(str)

# if need a list:
lst = list(string.ascii_lowercase)

# others
# help(string)

# ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# digits = '0123456789'
# hexdigits = '0123456789abcdefABCDEF'
# octdigits = '01234567'
# printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
# punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# whitespace = ' \t\n\r\x0b\x0c'



lst2 = list(map(chr, range(97, 123)) ) # 记得补多一位
print(lst2)

# 参数就是ascii table中的数字(0-127)
# 参数其实是unicode table,只是0-127也是ascii
print(chr(97))
print(chr(122))
print(chr(126))

