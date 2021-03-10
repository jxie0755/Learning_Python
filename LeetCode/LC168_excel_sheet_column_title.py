# LC168 Excel Sheet Column Tytle
# Easy


# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# 1-26: A-Z
# 27 - 702: AA - ZZ
# 703: AAA


class Solution(object):
    # Time:  O(logn)
    # Space: O(1)
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        translate = "ZABCDEFGHIJKLMNOPQRSTUVWXYZ"  # can be replaced by dict
        n -= 1
        body, tail = divmod(n, 26)
        tail_val = translate[tail]

        def process(body):
            if body == 0:
                return ""
            elif 0 < body <= 26:
                return translate[body - 1]
            else:
                return process(body // 26) + translate[body % 26 - 1]

        body_val = process(body)

        return body_val + tail_val

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        translate = "ZABCDEFGHIJKLMNOPQRSTUVWXYZ"
        n -= 1
        body, tail = divmod(n, 26)

        tail_val = translate[tail]
        body_val = ""
        while body != 0:
            if 1 < body <= 26:
                body_val = translate[body - 1] + body_val
                if body == 26:
                    body -= 1
            else:
                body_val = translate[body % 26 - 1] + body_val
            body = body // 26

        return body_val + tail_val


class Solution(object):
    # Time:  O(logn)
    # Space: O(1)
    def convertToTitle(self, n):
        translate = "ZABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        while n != 0:
            n, end = divmod(n, 26)
            if end == 0:
                n -= 1  # 减1位
            result = translate[end] + result

        return result


if __name__ == "__main__":
    assert Solution().convertToTitle(1) == "A", "Example 1"
    assert Solution().convertToTitle(27) == "AA", "Additional"
    assert Solution().convertToTitle(28) == "AB", "Example 2"
    assert Solution().convertToTitle(52) == "AZ", "Example 1"
    assert Solution().convertToTitle(701) == "ZY", "Example 3"
    assert Solution().convertToTitle(704) == "AAB", "Additional"

    print("All passed")
