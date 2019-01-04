# p551 Student Attendance Record I
# Easy

# You are given a string representing an attendance record for a student. The record only contains the following three characters:
# 'A' : Absent. 'L' : Late. 'P' : Present.
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
# You need to return whether the student could be rewarded according to his attendance record.
# 'LLL' is considered two 'LL'

# """
# :type s: str
# :rtype: bool
# """

class Solution:
    def checkRecord(self, s):
        ### return not s.count('A') > 1 and not s.count('LLL') > 0
        return s.count('A') <= 1 and 'LLL' not in s  # a better way of expression


if __name__ == '__main__':
    assert Solution().checkRecord('PPALLP') == True, 'regular good'
    assert Solution().checkRecord('PPALLAP') == False, 'two A and one LL'
    assert Solution().checkRecord('PPAPLLL') == False, 'one A with three LL'
    assert Solution().checkRecord('PAPALLPLLLL') == False, 'too bad'
    assert Solution().checkRecord('LALALALALALA') == False, 'bad bad'
    assert Solution().checkRecord('LLLLLLLL') == False, 'lazy guy'

    print('all passed')
