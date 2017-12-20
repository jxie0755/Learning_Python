# Input: Start and end date as datetime.date.
# Output: The quantity of the rest days as an integer.

from datetime import date, timedelta

def checkio(from_date, to_date):
    result = 0
    for i in range((to_date - from_date).days + 1):
        if from_date.isoweekday() == 6 or from_date.isoweekday() == 7:
            result += 1
        from_date += timedelta(days=1)  # 设置一个时间间隔为1天
        # 遍历过程从开始日期到结束日期(+1)检查weekday,符合周六周日的记入结果
    return result

if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"
    print('done')
