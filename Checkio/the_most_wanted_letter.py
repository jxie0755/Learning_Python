def checkio(text):
    text = text.lower()
    text = text.replace(' ', '')
    text_list = sorted(text)
    text_list.append('')
    text_dict = {}
    index = len(text_list)

    v = 1
    for i in range(0, index - 1):
        if text_list[i] == text_list[i + 1]:
            v += 1
        else:
            text_dict[text_list[i]] = v
            v = 1

    text_dict_filtered = {}
    for k, v in text_dict.items():
        if ord(k) >= 97 and ord(k) <= 122:
            text_dict_filtered[k] = v

    v_max = max(list(text_dict_filtered.values()))
    result_list = []
    for k in text_dict_filtered.keys():
        if text_dict_filtered[k] == v_max:
            result_list.append(k)

    result_list = sorted(result_list)
    return result_list[0]

print(checkio("Hello World!")) # == "l", "Hello test"
print(checkio("How do you do?")) # == "o", "O is most wanted"
print(checkio("One")) # == "e", "All letter only once."
print(checkio("Oops!")) # == "o", "Don't forget about lower case."
print(checkio("AAaooo!!!!")) # == "a", "Only letters."
print(checkio("abe")) # == "a", "The First."
print(checkio("a" * 9000 + "b" * 1000)) # == "a", "Long."
