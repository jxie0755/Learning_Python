text = 'aBc deCEfcf!!!!'
text = text.lower()
text = text.replace(' ', '')
text_list = sorted(text)
text_list.append('')
text_dict = {}
index = len(text_list)

v = 1
for i in range(0, index - 1):
    if text_list[i] == text_list[i+1]:
        v += 1
    else:
        text_dict[text_list[i]] = v
        v = 1

for k in text_dict.keys():
    if ord(k) < 97 or ord(k) > 122:
        del text_dict[k]

print(text_list)
print(text_dict)
