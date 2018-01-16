# class datetime 模块
# 模块常量
# datetime.MINYEAR
# date和datetime对象中允许的最小年份
import datetime

print(datetime.MINYEAR)  # >>> 1

# datetime.MAXYEAR
# date和datetime对象中允许的最大年份数
print(datetime.MAXYEAR)  # >>> 9999

# 可用类型
# class datetime.date
# class datetime.time
# class datetime.datetime
# class datetime.timedelta
# class datetime.tzinfo
# class datetime.timezone


datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

# timedelta对象表示时间的间隔，即两个日期或时间之间的差值。
datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# 所有参数都是可选的且默认为0。参数可以是整数或浮点数，也可以是正数或负数
dt = datetime.timedelta(1.5, 5.5, weeks=0.5)
print(dt)  # >>> 5 days, 0:00:05.500000


# 注意,timedelta只能在同类型的datetime class之间,不能跨越 (比如date-datetime)
# timedelta 不支持time之间的运算,只支持date和datetime, 除非通过datetime实例中y,m,d均为同一个值(1)来实现
# 原因: 不考虑时区来比较时间是不安全的,所以计算需要通过datetime确定日期,或者确定timezone才能安全的对比
datetimeX1 = datetime.datetime(1,1,1, 17, 00, 00)
datetimeX2 = datetime.datetime(1,1,1, 16, 30, 59)
print(datetimeX1-datetimeX2)  # >>> 0:29:01
# 或者使用datetime.strptime() (在datetime.strptime()中会介绍)


import datetime
A = datetime.timedelta(days=1, hours=2, seconds=100)  # 可以不用是整数,比如hour=0.5
print(A)                  # >>> 1 day, 2:01:40

# timedelta 类属性
print(datetime.timedelta.min)  # >>> -999999999 days, 0:00:00         # 注意,最小值不是0,而是类似(-max)的概念
print(datetime.timedelta.max)  # >>> 999999999 days, 23:59:59.999999
# timedelta.resolution
# 不相等的timedelta对象之间的最小可能差值，timedelta(microseconds=1)
