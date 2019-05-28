# P166 Fraction to Recurring Decimal
# Medium

# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.


class Solution(object):

    ### Version A
    ### DIY vresion of divide calculation like manual
    ### This will have to process movement of recur fraction
    def fractionToDecimal(self, a, b):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if a == 0:
            return '0'

        # 处理负数情况
        neg = False
        if a < 0 < b or b < 0 < a:
            neg = True
        a, b = abs(a), abs(b)

        ANS = ''
        remains_dict = {}
        remains_list = []
        recur = False

        def getFactor(a, b):
            factor = 0
            while a * 10 ** factor < b:
                factor += 1
            return factor

        while a != 0 and a not in remains_dict:

            if a >= b:
                val, remain = divmod(a, b)
                if not ANS:  # Just prepare ANS with > decimal point part
                    ANS = str(val)
                    if remain:  # do not record the divide calculation yet
                        ANS += '.'
                else: # only after the first divide calculation
                    remains_dict[a] = str(val)
                    remains_list.append(a)

            elif a < b:  # always record remains as a < b will generate decimal numbers
                factor = getFactor(a, b)
                new_a = a * 10 ** factor
                val, remain = divmod(new_a, b)
                lead_z = ''
                for i in range(factor - 1):
                    lead_z += '0'
                true_val = lead_z + str(val)
                remains_dict[a] = str(true_val)
                remains_list.append(a)
                if not ANS:
                    ANS = '0.'
            a = remain
            if a in remains_dict:
                recur = True

        # 如果没出现循环小数直接加起来
        if not recur:
            for i in remains_list:
                ANS += remains_dict[i]

        else:
            # 先找到绝对循环节之前的部分
            rec = ''
            rec_idx = -1
            for i in range(len(remains_list)):
                val = remains_list[i]
                if val == a:
                    rec_idx = i
                    break
                else:
                    ANS += remains_dict[val]

            # 找到绝对循环节
            for i in range(rec_idx, len(remains_list)):
                val = remains_list[i]
                rec += remains_dict[val]

            # 再考虑前移循环节
            for i in rec[::-1]:
                if i == ANS[-1]:
                    ANS = ANS[:-1]
                    rec = i + rec[:-1]
                else:
                    break

            ANS = ANS + '(' + rec + ')'

        return '-' + ANS if neg else ANS



if __name__ == '__main__':
    assert Solution().fractionToDecimal(0, 3) == '0', 'Edge'
    assert Solution().fractionToDecimal(-50, 8) == '-6.25', 'Edge Negative'

    assert Solution().fractionToDecimal(1, 2) == '0.5', 'Example 1'
    assert Solution().fractionToDecimal(2, 1) == '2', 'Example 2'
    assert Solution().fractionToDecimal(2,3) == '0.(6)', 'Example 3'

    assert Solution().fractionToDecimal(1,6) == '0.1(6)', 'Additional 1'
    assert Solution().fractionToDecimal(19,75) == '0.25(3)', 'Additional 2'
    assert Solution().fractionToDecimal(1,90) == '0.0(1)', 'Additional 3'
    assert Solution().fractionToDecimal(10,333) == '0.(030)', 'Additional 4'

    print('all passed')
