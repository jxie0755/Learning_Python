"""
string methods
https://docs.python.org/3/library/stdtypes.html#string-methods

No need to import string!!
"""

print()
print("str.capitalize()")
# Return a copy of the string with its first character capitalized and the rest lowercased.
print()
print("str.title()")
# Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.

# Notice the difference between capitalize() and title()
print("hello world".capitalize())  # >>> Hello world
print("hello world".title())       # >>> Hello World


print()
print("str.casefold()")
# Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.
# Casefolding is similar to casing but more aggressive because it is intended to remove all case distinctions in a string.
# German lowercase letter "ß" is equivalent to "ss". Since it is already lowercase, lower() would do nothing to "ß"; casefold() converts it to "ss".


print()
print("str.center(width)")
# Return centered in a string of length width.
print("str.rjust(width[, fillchar])")
# Return the string right justified in a string of length width.
print("str.ljust(width[, fillchar])")
# Return the string left justified in a string of length width.
# The original string is returned if width is less than or equal to len(s).

dd = "abc"
print(dd)           # >>> "abc"
print(dd.center(5)) # >>> " abc "
print(dd.center(6)) # >>> " abc  "     # 注意两边空白可能不等宽(奇偶问题),可以查len()
print(dd.center(7)) # >>> "  abc  "

print(dd)           # >>> "abc"
print(dd.rjust(5))  # >>> " abc"
print(dd.rjust(6))  # >>> "  abc"
print(dd.rjust(7))  # >>> "   abc"
print(dd)           # >>> "abc"
print(dd.ljust(5))  # >>> "abc "
print(dd.ljust(6))  # >>> "abc  "
print(dd.ljust(7))  # >>> "abc   "


print()
print("str.count(sub[, start[, end]])")
# Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.erpreted as in slice notation.
dd = ["a", "b", "c", "a"]
print(dd.count("a"))  # >>> 2
ee = "abcda"
print(ee.count("b"))  # >>> 1


print()
print("str.encode(encoding=”utf-8”, errors=”strict”)")
# Return an encoded version of the string as a bytes object.


print()
print("str.startswith(prefix[, start[, end]])")
# Return True if string starts with the prefix, otherwise return False.
dd = "abcabc"
print(dd.startswith("abc"))  # >>> True


print()
print("str.endswith()")
# Return True if the string ends with the specified suffix, otherwise return False.
dd = "abc"
print(dd.endswith("b"))  # >>> False
print(dd.endswith("c"))  # >>> True
ee = "123\n"
print(ee.endswith("\n")) # >>> True


print()
print("str.expandtabs(tabsize=8)")
# Return a copy of the string where all tab characters are replaced by one or more spaces, depending on the current column and the given tab size.
dd = "\tabc"
print(dd)               # >>>  "    abc"
print(dd.expandtabs())  # >>>  "        abc"


print()
print("str.find(sub[, start[, end]])")
print("str.index(sub[, start[, end]])")

print("str.rfind(sub[, start[, end]])")
print("str.rindex(sub[, start[, end]])")
# The find() method should be used only if you need to know the position of sub. To check if sub is a substring or not, use the in operator:

# 能找到的时候,给出第一个index
dd = "abcaC"
print(dd.find("ab"))  # >>> 0
print(dd.find("a"))   # >>> 0
print(dd.find("d"))   # >>> -1
# print(dd.index("d"))  # >>> ValueError
print(dd.find("C"))   # >>> 4

# rfind和rindex非常类似,只是找的是最后一个index而不是第一个


print()
print("str.format(*args, **kwargs)")
# Perform a string formatting operation.
# python 3.6 new feature, simplified when variable and string mixed together than
# "string{}".format()

name = "Denis"
name2 = "Cindy"
print("hello, {}, {}".format(name, name2))
print(f"hello, {name}, {name2}")       # recommended (f-string)
# >>>
# hello, Denis, Cindy
# hello, Denis, Cindy

text = "abc"

print("Text: {!r}\n".format(text))  # >>> Text: "abc"
print(f"Text: {text!r} \n")         # >>> Text: "abc"
# execute function in f-string
pi = 3.14159
radius = 10
def area_of_circle(radius):
    return 2*pi*radius
print(f"Area of a circle with radius {radius}: {area_of_circle(radius=radius)}")
# >>> "Area of a circle with radius 10: 62.8318"


print()
print("str.isalnum()")
# Return true if all characters in the string are alphanumeric and there is at least one character, false otherwise.
"ABCabc1".isalnum()   # >>> True
"ABC abc1".isalnum()  # >>> False


print()
print("str.isalpha()")
# Return true if all characters in the string are alphabetic and there is at least one character, false otherwise.
"ABCabc".isalpha()   # >>> True
"ABCabc1".isalpha()  # >>> False


print()
print("str.isdigit()")
# Return true if all characters in the string are digits and there is at least one character, false otherwise.


print()
print("str.isdecimal()")
# Return true if all characters in the string are decimal characters and there is at least one character, false otherwise.


print()
print("str.isnumeric()")
# Return true if all characters in the string are numeric characters, and there is at least one character, false otherwise.

# isdecimal, isnumeric, isdigits 区别


print()
print("str.isidentifier()")
# Return true if the string is a valid identifier according to the language definition, section Identifiers and keywords.
# Use keyword.iskeyword() to test for reserved identifiers such as def and class.
dd = "str"
print(dd.isidentifier())  # >>> True


print()
print("str.islower()")
# Return true if all cased characters in the string are lowercase and there is at least one cased character, false otherwise.


print()
print("str.isupper()")
# Return true if all cased characters in the string are uppercase and there is at least one cased character, false otherwise.

print()
print("str.lower()")
# Return a copy of the string with all the cased characters converted to lowercase.

print()
print("str.upper()")
# Return a copy of the string with all the cased characters converted to uppercase.


print()
print("str.join(iterable)")
# Return a string which is the concatenation of the strings in iterable.
dd = ["1", "2", "3"]
print("*".join(dd))  # >>> "1*2*3"


print()
print("str.isprintable()")
# Return true if all characters in the string are printable or the string is empty, false otherwise.
# Nonprintable characters are those characters defined in the Unicode character database as “Other” or “Separator”, excepting the ASCII space (0x20) which is considered printable.


print()
print("str.isspace()")
# Return true if there are only whitespace characters in the string and there is at least one character, false otherwise.
# Whitespace characters are those characters defined in the Unicode character database as “Other” or “Separator” and those with bidirectional property being one of “WS”, “B”, or “S”.


print()
print("str.istitle()")
# Return true if the string is a titlecased string and there is at least one character. Return false otherwise.


print()
print("str.maketrans(x[, y[, z]])")
print("str.translate")
# maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。两个字符串的长度必须相同，为一一对应的关系。
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
print(trantab)  # 输出一个ascii字符对应dict
# >>> {97: 49, 101: 50, 105: 51, 111: 52, 117: 53}

test = "this is string example....wow!!!"
print(test.translate(trantab))  # 将test中的字符依依对换
# >>> th3s 3s str3ng 2x1mpl2....w4w!!!


print()
print("str.replace(old, new[, count])")
# Return a copy of the string with all occurrences of substring old replaced by new.
# If the optional argument count is given, only the first count occurrences are replaced.

test = "this is string example....wow!!!"
print(test
      .replace("a", "1")
      .replace("e", "2")
      .replace("i", "3")
      .replace("o", "4")
      .replace("u", "5")
      )
# >>> th3s 3s str3ng 2x1mpl2....w4w!!!
# 与makestrans类似,但是一次替换一个

test = "this is string example....wow!!!"
print(test.replace("i", "9"))     # >>> th9s 9s str9ng example....wow!!!
print(test.replace("i", "9", 2))  # >>> th9s 9s string example....wow!!!  # notice that not all "i" was replaced, only 2 were.


print()
print("str.swapcase()")
# Return a copy of the string with uppercase characters converted to lowercase and vice versa.
# Note that it is not necessarily true that s.swapcase().swapcase() == s.

print("Hello World".swapcase()) # >>> "hELLO wORLD"


print()
print("str.lstrip([chars])")
print("str.rstrip([chars])")
print("str.strip([chars])")
# string all the space and escape of a string

dd = "   abc   "
print(dd.lstrip())  # >>> "abc   "
print(dd.rstrip())  # >>> "   abc"
print(dd.strip())   # >>> "abc"
# "\n"也会被remove

dd = "abcDDD"
print(dd.lstrip("abc"))  # >>> "DDD"
print(dd.lstrip("ac"))   # >>> "bcDDD"
print(dd.rstrip("D"))    # >>> "abc"
print(dd.strip("aD"))    # >>> 'b


print()
print("str.split(sep=None, maxsplit=-1)")
# Return a list of the words in the string, using sep as the delimiter string.
print("str.rsplit(sep=None, maxsplit=-1)")
# Return a list of the words in the string, using sep as the delimiter string.

dd = "abcabc"
print(dd.split("c"))   # >>> ["ab", "ab", ""]
print(dd.rsplit("c"))  # >>> ["ab", "ab", ""]

dd = "1      2       3"
print(dd.rsplit(maxsplit=1))  # >>> ["1      2", "3"]
print(dd.split(maxsplit=1))   # >>> ["1", "2      3"]
# If maxsplit is given, at most maxsplit splits are done, the rightmost ones.

# If sep is not specified or None, any whitespace string is a separator.
dd = "abc abc"
print(dd.split())  # >>> ["abc", "abc"]

"1,2,3".split(",")              # >>> ["1", "2", "3"]
"1,2,3".split(",", maxsplit=1)  # >>> ["1", "2,3"]
"1,2,,3,".split(",")            # >>> ["1", "2", "", "3", ""]  # 每次split都在目标两旁有string,所以要创造""来填补

"1 2 3".split()                # >>> ["1", "2", "3"]
"1 2 3".split(maxsplit=1)      # >>> ["1", "2 3"]
"   1   2   3   ".split()      # >>> ["1", "2", "3"]


print()
print("str.splitlines([keepends])")
# Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.
dd = "abc\nabc"
print(dd.splitlines())  # >>> ["abc", "abc"]


print()
print("str.partition(sep)")
# Split the string at the first occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing the string itself, followed by two empty strings.


print()
print("str.rpartition(sep)")
# Split the string at the last occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. I

dd = "abcabc"
print(dd.partition("c"))   # >>> ("ab", "c", "abc")
print(dd.rpartition("c"))  # >>> ("abcab", "c", "")  # r~~ find the last separatio


print()
print("str.zfill(width)")
# Return a copy of the string left filled with ASCII "0" digits to make a string of length width. A leading sign prefix ("+"/"-") is handled by inserting the padding after the sign character rather than before.
print("42".zfill(5)) # >>> "00042"
print("-42".zfill(5)) # >>> "-0042"
