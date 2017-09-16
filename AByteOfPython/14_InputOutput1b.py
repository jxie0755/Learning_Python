# Input Output 1b:

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

while True:                   # 先设置循环, 把input包括在循环中,这样每次循环才让人输入内容
    something = input("Enter text: ")
    if something == 'quit':
        break
    if is_palindrome(something):
        print("Yes, it s a palindrome")
    else:
        print("No, it is not a palindrome")
