def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

import unittest

class PnumTest(unittest.TestCase):
    """Test isPrime()"""
    def test_prime_number(self):
        self.assertTrue(isPrime(97))
    def test_not_prime_number(self):
        self.assertFalse(isPrime(98))
unittest.main()
