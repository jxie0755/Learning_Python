# http://www.pythonchallenge.com/pc/def/map.html
print()
def letter_push(raw_text):
    new_text = ''
    for i in raw_text:
        if ord(i) in range(65, 89) or ord(i) in range(97, 121):
            new_i = chr(ord(i)+2)
            new_text += new_i
        elif ord(i) == 89:
            new_text += 'A'
        elif ord(i) == 90:
            new_text += 'B'
        elif ord(i) == 121:
            new_text += 'a'
        elif ord(i) == 122:
            new_text += 'b'
        else:
            new_text += i

    print(new_text)
    return(new_text)

raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

letter_push(raw)
print()
letter_push('map')
