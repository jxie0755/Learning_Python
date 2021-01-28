"""
https://leetcode.com/problems/restore-ip-addresses/
P093 Restore IP Addresses
Medium


Given a string containing only digits, restore it by returning all possible valid IP address combinations.
"""

from typing import *


class Solution_A:
    def restoreIpAddresses(self, s: str) -> List[str]:
        pass


if __name__ == "__main__":
    testCase = Solution_A()

    assert testCase.restoreIpAddresses("0000") == ["0.0.0.0"], "Edge 1"
    assert testCase.restoreIpAddresses("01000") == ["0.10.0.0"], "Edge 2"

    assert testCase.restoreIpAddresses("25525511135") == ["255.255.11.135", "255.255.111.35"], "Example 1"

    print("All passed")
