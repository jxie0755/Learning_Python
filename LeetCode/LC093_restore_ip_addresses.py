"""
https://leetcode.com/problems/restore-ip-addresses/
P093 Restore IP Addresses
Medium


Given a string containing only digits, restore it by returning all possible valid IP address combinations.
"""

from typing import *


class Solution_A1:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        Branch recursive method with helper to step by step add each of 4 groups to form IP address
        Each IP address can maximally be 3 digit long, branch by digit length
        Validify each group, and only proceed recursion if valid
        Add to result when all 4 groups are valid
        """
        result = []

        def restoreIpHelper(s: str, address: str = "", parts: int = 0):
            """
            A branch recursive helper (internal)
            """
            L = min(3, len(s))

            if parts < 3:  # first 3 groups, with different length branching
                for i in range(1, L + 1):
                    group = s[:i]
                    rest = s[i:]
                    # [single digit] or [double digit, but not start with "0" and ensure digit <= 255]
                    if len(group) == 1 or (len(group) > 1 and group[0] != "0" and int(group) <= 255):
                        restoreIpHelper(rest, address + group + ".", parts + 1)

            elif parts == 3:  # last group, ensure all the rest of s make a valid last group
                if len(s) == 1 or (len(s) > 1 and s[0] != "0" and int(s) <= 255):
                    restoreIpHelper("", address + s, parts + 1)

            else:  # end case to add finished address to result
                result.append(address)

        restoreIpHelper(s)
        return result


class Solution_A2:
    RESULT = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        Same principle as Version A1, but move the helper external
        """
        self.restoreIpHelper(s)
        ans = self.RESULT.copy()  # transfer answer to a new list
        self.RESULT.clear()       # remember to wipe RESULT for next run
        return ans

    def restoreIpHelper(self, s: str, address: str = "", parts: int = 0):
        """
        A branch recursive helper (external)
        """
        L = min(3, len(s))

        if parts < 3:  # first 3 groups, with different length branching
            for i in range(1, L + 1):
                group = s[:i]
                rest = s[i:]
                # [single digit] or [double digit, but not start with "0" and ensure digit <= 255]
                if len(group) == 1 or (len(group) > 1 and group[0] != "0" and int(group) <= 255):
                    self.restoreIpHelper(rest, address + group + ".", parts + 1)

        elif parts == 3:  # last group, ensure all the rest of s make a valid last group
            if len(s) == 1 or (len(s) > 1 and s[0] != "0" and int(s) <= 255):
                self.restoreIpHelper("", address + s, parts + 1)

        else:  # end case to add finished address to result
            self.RESULT.append(address)



if __name__ == "__main__":
    testCase = Solution_A2()

    assert testCase.restoreIpAddresses("0000") == ["0.0.0.0"], "Edge 1"
    assert testCase.restoreIpAddresses("01000") == ["0.10.0.0"], "Edge 2"

    assert testCase.restoreIpAddresses("25525511135") == ["255.255.11.135", "255.255.111.35"], "Example 1"

    print("All passed")
