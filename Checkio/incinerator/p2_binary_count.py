# You are given a number (a positive integer).
# You should convert it to the binary format and count how many unities (1) are in the number spelling.
# For example: 5 = 0b101 contains two unities, so the answer is 2.

# Input: A number as a positive integer.
# Output: The quantity of unities in the binary form as an integer.

def checkio(number):
    return bin(number)[2:].count('1')  # bin() output is a string already.

if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
    print('done')
