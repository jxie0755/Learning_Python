def checkio(text):
    # raw string process, transfer to lower case and remove spaces
    text = text.lower()
    text = text.replace(' ', '')
    # raw string process 2, create a list, sort and add an empty string at the end.
    text_list = sorted(text)
    for i in text_list:
        if ord(i) < 97 or ord(i) > 122:
            text_list.remove(i)

    text_list.append('')
    # raw string process 3, create a dict for each character and number of occurrence
    text_dict = {}

    # a loop to add data to the dict
    index = len(text_list)
    v = 1
    for i in range(0, index - 1):
        if text_list[i] == text_list[i + 1]:
            v += 1
        else:
            text_dict[text_list[i]] = v
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

# Passed
