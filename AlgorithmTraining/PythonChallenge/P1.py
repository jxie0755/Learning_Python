# http://www.pythonchallenge.com/pc/def/map.html
raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
import string
def char_move(n):
    a = str(string.ascii_lowercase)
    b = a[n:] + a[:n]
    dict = str.maketrans(a, b)
    return dict
    
print(raw.translate(char_move(2)))
print("map".translate(char_move(2)))
