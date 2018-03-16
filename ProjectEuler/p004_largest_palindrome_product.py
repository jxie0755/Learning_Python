# P003 Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Brutal force method
# define a function to check if palindrome
def isPalindrome(n):
    return str(n) == str(n)[::-1]

# define a function to conduct the brutal force search
def search_largest_palindrome():
    """search the largest 6 digit padlindrome number"""

    # define the boundary
    maximum = 999 * 999
    minimum = 100 * 100

    # Create an iterator the filter the 6 digit padlindrome numbers from big to small
    palindrome_list = filter(isPalindrome, range(maximum, minimum - 1, -1))

    for number in palindrome_list:
        for divisor in range(100, 1000):
            other_divisor = number // divisor
            if number % divisor == 0 and other_divisor in range(100, 1000):
                print(number, 'by', divisor, '*', other_divisor)
                return number

print(search_largest_palindrome())
# >>>
# 906609 by 913 * 993
# 906609

