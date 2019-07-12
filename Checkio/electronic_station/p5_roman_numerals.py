# p5_roman_numerals

# The first ten Roman numerals are: I, II, III, IV, V, VI, VII, VIII, IX, and X.
Roman_Nu = {"I" : 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
Roman_Nu = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
# For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.
# Input: A number as an integer.
# Output: The Roman numeral as a string.

# 注意dictionary的order问题

# Version 1 Exhaustive method
def checkio(data):
    R = {0:"", 1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX",
         10:"X", 20:"XX", 30:"XXX", 40:"XL", 50:"L", 60:"LX", 70:"LXX", 80:"LXXX", 90:"XC",
         100:"C", 200:"CC", 300:"CCC", 400:"CD", 500:"D", 600:"DC", 700:"DCC", 800:"DCCC", 900:"CM",
         1000:"M", 2000:"MM", 3000:"MMM"}
    
    data = str(data).rjust(4, "0")   # 利用rjust补足数字成为4位数
    dlst = list(map(lambda x,y: int(x)*y, data, (1000, 100, 10, 1)))  # 分解各数位
    return  "".join(list(map(lambda x: R[x], dlst))) # 将各数位代换成罗马数字,然后拼接


# Version 2 Calculation
def checkio2(data):
    data = str(data).rjust(4, "0")  # 拆解data成为单独的数字字符,并补足数位
    def rom(n, x, y, z):   # 写一个函数来表明转换逻辑
        nd = int(data[n])
        if nd == 0:
            return ""
        elif nd < 4:
            return nd*x
        elif nd == 4:
            return x + y
        elif nd < 9:
            return y + (nd-5) * x
        elif nd == 9:
            return x + z
    
    # 使用map对data中每个数位进行转换,然后合并
    return "".join(list(map(rom, range(4), ["M","C","X","I"], ["","D","L","V"], ["","M","C","X"])))

# Version 3 divmod method, 直接对数字进行转换,而不是字符操作
def checkio3(data):
    result = ""
    roman_dict = {1000: "M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
    for arabic, roman in roman_dict.items():
        repeat, data = divmod(data, arabic)
        result += repeat * roman
    return result

if __name__ == "__main__":
    assert checkio3(4) == "IV"
    assert checkio3(6) == "VI", "6"
    assert checkio3(76) == "LXXVI", "76"
    assert checkio3(499) == "CDXCIX", "499"
    assert checkio3(3888) == "MMMDCCCLXXXVIII", "3888"
