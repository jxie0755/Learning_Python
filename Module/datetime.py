# class datetime 模块

# 可用类型
# class datetime.date
# class datetime.time
# class datetime.datetime
# class datetime.timedelta
# class datetime.tzinfo
# class datetime.timezone


# datetime.timedelta

# timedelta对象表示时间的间隔，即两个日期或时间之间的差值。
# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# 所有参数都是可选的且默认为0。参数可以是整数或浮点数，也可以是正数或负数

import datetime

A = datetime.timedelta(days=1, hours=2, seconds=100)  # 可以不用是整数,比如hour=0.5
print(A)  # >>> 1 day, 2:01:40
print(A.days)  # >>> 1     # just day
print(A.seconds)  # >>> 7300  # 此处把hours也转换成秒(1天内的秒数)
print(A.total_seconds())  # >>> 131500.0
print(A.microseconds)  # >>> 500   # just microseconds
# days属性可以取负值，另外两个属性都只能是正值

# datetime.date(year, month, day)
# date对象

import datetime

datetime.date(2017, 11, 9)  # 指定一个date
datetime.date.today()  # 返回当前本地的日期。这相当于date.fromtimestamp(time.time())

datetime.date.min  # >>> 0001-01-01
datetime.date.max  # >>> 9999-12-31

import datetime

print(datetime.date(1986, 6, 7))  # >>> 1986-06-07
print(datetime.date.today())  # >>> 2017-11-09

A = datetime.date(2017, 11, 8)
print(A.year)  # >>> 2017
print(A.month)  # >>> 11
print(A.day)  # >>> 8
print(A.resolution)  # >>> 1 day, 0:00:00

A = datetime.date(2017, 11, 8)
B = datetime.date(2016, 11, 8)
C = B - A
D = A - B
print(C)  # >>> -365 days, 0:00:00
print(D)  # >>>  365 days, 0:00:00
# 此处C为timedelta
# 测试闰年 - 成功- 会计算出366天

A = datetime.date(2017, 8, 8)
A.replace(year=2016, month=7, day=7)
B = A.replace(year=2016, month=7, day=7)
print(A)  # >>> 2017-08-08 # A不会因为replace被改变.
print(B)  # >>> 2016-07-07 # 可以使用关键字(year, month, day),修改局部数据

A = datetime.date(2017, 8, 8)
print(A.timetuple())
# >>> time.struct_time(tm_year=2017, tm_mon=8, tm_mday=8, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=220, tm_isdst=-1)
# tm_wday - (0-6): Mon = 0, Sun = 6
# tm_yday: 这是今年的第几天(1月1号是第一天,不是第零天)

print(A.toordinal())  # >>> 736549  # 返回公历日期的序数，其中第1年的1月1日为第1天。
print(A.weekday())  # >>> 1  # same as tm_wday.(0-6): Mon = 0, Sun = 6
print(A.isoweekday())  # >>> 2  # 竟然不一样, (1-7): Mon = 1, Sun = 7
print(A.isocalendar())  # >>> (2017, 32, 2) 从1开始计算, 第2017年的第32周的第2天
print(A.isoformat())  # 2017-08-08 # YYYY-MM-DD
print(A.__str__())  # 对于日期d，str(d)等同于d.isoformat()
print(A.strftime('%m/%d/%y'))  # >>> 08/08/17
print(A.strftime('%m/%d/%y %H:%M:%S'))  # >>> 08/08/17 00:00:00
print(A.__format__("%d/%m/%y"))  # same as above


# datetime.datetime 对象
# 基本就是date + time

print(datetime.datetime(year=2017, month=3, day=15, hour=17, minute=15, second=30))
# >>> 2017-03-15 17:15:30
# all (year, month, day, hour, minute, second, microsecond, tzinfo=None)

print(datetime.datetime.today())  # >>> 2017-11-09 21:08:32.589043 精确到毫秒
print(datetime.datetime.now())  # 若无tz,则基本等于today()
print(datetime.datetime.utcnow())  # 返回当前UTC日期和时间
print(A.fromordinal(365))  # 0001-12-31 00:00:00   公元后xx天的日期    # 只接受天数作为参数
print(A.toordinal())  # 736403                相距公元-天数       # 只返回天数

print(A.strftime('%m/%d/%y %I:%M:%S %p'))  # >>> 03/16/17 05:15:30 PM
print(A.year)  # >>> 2017
print(A.month)  # >>> 3
print(A.day)  # >>> 16
print(A.hour)  # >>> 17
print(A.minute)  # >>> 15
print(A.second)  # >>> 30
print(A.microsecond)  # >>> 0

# 除此同样也有一下方法
# .weekday()
# .isoweekday()
# .isocalendar()
# .isoformat()
# 可选参数sep（默认为
# 'T'）
# .__str__()
