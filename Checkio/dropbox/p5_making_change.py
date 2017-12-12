# When making purchases, Nicola would like to use the minumum number of coins possible.
# For example, Outer Leftopia has coins with denomination 1, 3, and 5 shillings.

# Input: Two arguments. The first argument is an int: the price of the purchase. The second is a list of ints: the denominations of available coins.
# Output: int. The minimum number of coins Nicola can use to make the purchase. If the price cannot be made with the available denominations, return None.

def checkio(price, denominations):
    """
        return the minimum number of coins that add up to the price
    """
    return None

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(8, [1, 3, 5]) == 2
    assert checkio(12, [1, 4, 5]) == 3
    print('Done')
