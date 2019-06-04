# P011 Container with Most Water
# Medium

# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0)
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.


# Note: You may not slant the container and n is at least 2.


class Solution:
    def maxArea(self, height):
        # Brutal force will be O(N^2), Time Limit Exceeded
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        result = []
        while i != len(height) -1:
            first = height[i]
            j = i + 1
            while j != len(height):
                second = height[j]
                volume = min(first, second) * (j - i)
                result.append(volume)
                j += 1
            i += 1
        return max(result)

    def maxArea(self, height):
        # find the heighest two, and check volume, then find the next highest two
        # O(N^2) in worst case, but sometimes O(log n * N)
        # Still exceeded max time limit on a case of ascending numbers.
        """
        :type height: List[int]
        :rtype: int
        """
        result = []
        hashtable = dict(enumerate(height))
        tops = {}

        def obtain_top(hstble):
            """得到hashtable中最大值的index"""
            i = max(hstble, key=hstble.get)
            tops[i] = hstble[i] # 转移到tops字典, 也就是记录最大值的字典
            del hstble[i]  # 记住要删掉这个最大值

        def remove_between(hstble):
            """删除最高值之间的所有数据"""

            # 先得到tops中,两个距离最远的柱子的index
            start, end = min(hstble), max(hstble)

            # 把这两个距离最远的柱子的装水体积算出来,添加到result
            result.append(min(hstble[start], hstble[end]) * (end - start))

            # 然后把两个柱子之间的数据删除
            for i in range(start + 1, end):
                if i in hashtable:
                    del hashtable[i]

        # 首先得到第一个最大值
        obtain_top(hashtable)

        # 然后得到第二个最大值, 开始循环添加装水体积和删除之间的数据
        while len(hashtable) != 0:  # 若原始数据被删空则停止
            obtain_top(hashtable)
            remove_between(tops)

        return max(result)


    def maxArea(self, height):
        # Start from both end, move the shorter side closer, to compare the possibe volume
        # O(N) locked, best answer
        max_area, i, j = 0, 0, len(height) - 1
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area



if __name__ == '__main__':
    assert Solution().maxArea([0, 0]) == 0, 'Edge 1'
    assert Solution().maxArea([0, 0, 0]) == 0, 'Edge 2'

    assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49, 'Example 1'
    assert Solution().maxArea([2,3,0,0,3,0,0,0,0,2]) == 18, 'Example 2'
    assert Solution().maxArea([2,3,4,5,6,7,8,9,100,100]) == 100, 'Example 3'
    assert Solution().maxArea([1,1,1,1,1,10,10,1,1,1,1,1]) == 11, 'Example 4'
    assert Solution().maxArea([1,1,4,1,5,5,4,1,1,1]) == 16, 'Example 5'

    print('All passed')
