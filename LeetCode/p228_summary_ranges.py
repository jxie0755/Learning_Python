# P228 Summary Ranges
# Medium


# Given a sorted integer array without duplicates, return the summary of its ranges.


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        nums = nums + [float('inf')]
        result = []
        rangefound = False

        temp = ''
        i = 0
        while i != len(nums)-1:
            cur, nex = nums[i], nums[i+1]
            if nex != cur + 1:
                if rangefound:
                    temp += str(cur)
                    result.append(temp)
                    temp = ''
                else:
                    result.append(str(cur))
                rangefound = False
            else:
                rangefound = True
                if not temp:
                    temp += str(cur) + '->'
            i += 1
        return result

print(Solution().summaryRanges([0,2,3,4,6,8,9]))



if __name__ == '__main__':
    assert Solution().summaryRanges([]) == [], 'Edge'

    assert Solution().summaryRanges([0,1,2,4,5,7]) == ["0->2","4->5","7"], 'Example 1'
    assert Solution().summaryRanges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"], 'Example 2'

    print('all passed')
