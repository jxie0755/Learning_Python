# P165 Compare Version Numbers
# Medium


# Compare two version numbers version1 and version2.
# If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

# You may assume that the version strings are non-empty and contain only digits and the . character.

# The . character does not represent a decimal point and is used to separate number sequences.

# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

# You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.

# Note:
# Version strings are composed of numeric strings separated by dots . and this numeric strings may have leading zeroes.
# Version strings do not start or end with dots, and they will not be two consecutive dots.


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(i) for i in version1.split(".")]
        v2 = [int(i) for i in version2.split(".")]

        def helper(lst1, lst2):
            """recursive helper to compare the list values"""
            if lst1 and lst2:
                v1_val, v2_val = lst1[0], lst2[0]
                if v1_val > v2_val:
                    return 1
                elif v1_val < v2_val:
                    return -1
                else:
                    return helper(lst1[1:], lst2[1:])
            elif lst1 or lst2:
                if lst1:
                    N = len(lst1)
                    for i in range(N):
                        if lst1[i] != 0:
                            return 1
                    else:
                        return 0
                elif lst2:
                    N = len(lst2)
                    for i in range(N):
                        if lst2[i] != 0:
                            return -1
                    else:
                        return 0
            else:
                return 0

        return helper(v1, v2)


if __name__ == "__main__":
    assert Solution().compareVersion("0.1", "1.1") == -1, "Example 1"
    assert Solution().compareVersion("1.0.1", "1") == 1, "Example 2"
    assert Solution().compareVersion("7.5.2.4", "7.5.3") == -1, "Example 3"
    assert Solution().compareVersion("1.01", "1.001") == 0, "Example 4, ignore leding zero"
    assert Solution().compareVersion("1.0", "1.0.0") == 0, "Example 5"

    print("all passed")
