# P093 Restore IP Addresses
# Medium


# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

from typing import *


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4:
            return []

        addresses = []

        def helper(ss, result, nodes):
            if nodes < 0:
                pass
            elif nodes == 1 and len(ss) > 3:
                pass
            elif nodes == 0 and len(result) == 4 + len(s):
                addresses.append(result[:-1])
            else:
                L = 4
                if len(ss) < 3:
                    L = len(ss) + 1
                for i in range(1, L):
                    head, tail = ss[0:i], ss[i:]
                    if head == "0":
                        helper(ss[1:], result + "0.", nodes - 1)
                        break
                    elif head and int(head) <= 255:
                        new_result = result + head + "."
                        helper(tail, new_result, nodes - 1)

        helper(s, "", 4)
        return addresses


if __name__ == "__main__":
    assert Solution().restoreIpAddresses("0000") == ["0.0.0.0"], "Edge 1"
    assert Solution().restoreIpAddresses("01000") == ["0.10.0.0"], "Edge 2"

    assert Solution().restoreIpAddresses("25525511135") == ["255.255.11.135", "255.255.111.35"], "Example 1"

    print("All passed")
