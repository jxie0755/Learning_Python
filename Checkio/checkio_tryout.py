import string
text = 'adbc!!!'
text = ''.join(sorted(list(''.join(filter(lambda x: x in string.ascii_lowercase, text.lower())))))

print(text)
