# p014 Longest Common Prefix
# Easy

# Write a function to find the longest common prefix string amongst an array of strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        result = ''
        for i in range(len(min(strs, key=len))):
            temp = []
            for j in range(len(strs)):
                temp.append(strs[j][i])
            print(temp)
            if len(set(temp)) == 1:
                result += temp[0]
            else:
                break
        return result
# beat 53.82% python submission

lst = ['Denis Xie', 'Dennis X', 'Dendi Den', 'Deln']
lst2 = ["aca", "cba"]
print(Solution().longestCommonPrefix(lst2))  # >>> Den
