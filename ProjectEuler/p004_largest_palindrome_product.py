# P003 Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 Ã— 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Brutal force method


# define a function to conduct the brutal force search
def search_largest_palindrome(min_prod, max_prod):
    """search the largest 6 digit padlindrome number"""

    # Create an generator the filter the 6 digit padlindrome numbers from big to small
    def genPadlindromes():
        maximum, minimum = max_prod ** 2, min_prod ** 2
        for number in range(maximum, minimum - 1, -1):
            if str(number) == str(number)[::-1]:
                yield number

    palindrome_numbers = genPadlindromes()
    limit = range(min_prod, max_prod + 1)
    running = True
    while running:
        try:
            sample = next(palindrome_numbers)
            for divisor in limit:
                other_divisor = sample // divisor
                if sample % divisor == 0 and other_divisor in limit:
                    print(sample, 'by', divisor, '*', other_divisor)
                    return sample
        except StopIteration:
            running = False

if __name__ == '__main__':
    assert search_largest_palindrome(10, 99) == 9009, 'regular'
    print(search_largest_palindrome(100, 999))
    # >>>
    # 906609 by 913 * 993
    # 906609
    # passed
