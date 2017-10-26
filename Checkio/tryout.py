# text = 'aBc deCEfcf!!!!'
text = 'aabbcceeddffgg'
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

text_dict_filtered = {}
for k, v in text_dict.items():
    if ord(k) >= 97 and ord(k) <= 122:
        text_dict_filtered[k] = v

if

v_max = max(list(text_dict_filtered.values()))
for k in text_dict_filtered.keys():
    if text_dict_filtered[k] == v_max:
        print(k)


print(text_list)
print(text_dict_filtered)

