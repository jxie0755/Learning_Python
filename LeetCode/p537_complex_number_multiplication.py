# p537 Complex Number Multiplication
# Medium

# Given two strings representing two complex numbers.
# You need to return a string representing their multiplication. Note i2 = -1 according to the definition.
# Note:
# The input strings will not have extra blank.
# The input strings will be given in the form of a+bi, where the integer a and b will both belong to the
# range of [-100, 100]. And the output should be also in this form.

# """
# :type a: str
# :type b: str
# :rtype: str
# """

class Solution:
    def complexNumberMultiply(self, a, b):
        # find index to separate two parts, and extract the integers out

        i_a, i_b = a.find("+"), b.find("+")
        a1, a2, b1, b2 = a[:i_a], a[i_a+1:], b[:i_b], b[i_b+1:]
        int_a1, int_a2, int_b1, int_b2 = int(a1), int(a2[:-1]), int(b1), int(b2[:-1])

        # calculation logic and string output
        result_first = str(int_a1 * int_b1 + -1 * int_a2 * int_b2)
        result_second = str(int_a1 * int_b2 + int_a2 * int_b1)
        return result_first + "+" + result_second + "i"

    def complexNumberMultiply(self, a, b):
        # a better way to extract integers by using map()
        int_a1, int_a2 = map(int, a[:-1].split("+"))
        int_b1, int_b2 = map(int, b[:-1].split("+"))
        return f"{int_a1 * int_b1 - int_a2 * int_b2}+{int_a1 * int_b2 + int_a2 * int_b1}i"
        # LeetCode not support f-string yet

if __name__ == "__main__":
    assert Solution().complexNumberMultiply("1+1i", "1+1i") == "0+2i", "positive test"
    assert Solution().complexNumberMultiply("1+-1i", "1+-1i") == "0+-2i", "negative test"
    print("all passed")
