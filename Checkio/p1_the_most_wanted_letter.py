def checkio(text):
    # raw string process, transfer to lower case and remove spaces
    text = text.lower()
    text = text.replace(' ', '')

    # raw string process 2, create a list, sort and add an empty string at the end.
    text_list = sorted(text)
    text_list_clean = []
    for i in text_list:
        if ord(i) >= 97 and ord(i) <= 122:
            text_list_clean.append(i)
    text_list_clean.append('')

    # create an empty dict and a loop to add data to the dict
    text_dict = {}
    index = len(text_list_clean)
    v = 1
    for i in range(0, index - 1):
        if text_list_clean[i] == text_list_clean[i + 1]:
            v += 1
        else:
            text_dict[text_list_clean[i]] = v
            v = 1

    # generate a list that stores all the values
    v_max = max(list(text_dict.values()))
    for k in text_dict.keys():
        if text_dict[k] == v_max:
            break
    return k

print(checkio("Hello World!"))  # == "l", "Hello test"
print(checkio("How do you do?"))  # == "o", "O is most wanted"
print(checkio("One"))  # == "e", "All letter only once."
print(checkio("Oops!"))  # == "o", "Don't forget about lower case."
print(checkio("AAaooo!!!!"))  # == "a", "Only letters."
print(checkio("abe"))  # == "a", "The First."
print(checkio("a" * 9000 + "b" * 1000))  # == "a", "Long."
print(checkio('Lorem ipsum dolor sit amet 0000000000000000000!!!'))  # == 'm'


# Passed
