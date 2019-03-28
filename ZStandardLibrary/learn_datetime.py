# datetime module
# https://docs.python.org/3/library/datetime.html#module-datetime


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

print()
print('class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)')

# timedelta对象表示时间的间隔，即两个日期或时间之间的差值。
datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# 所有参数都是可选的且默认为0。参数可以是整数或浮点数，也可以是正数或负数
dt = datetime.timedelta(1.5, 5.5, weeks=0.5)
print(dt)  # >>> 5 days, 0:00:05.500000

# timedelta对象是可哈希的（可用作字典键）
# 注意,timedelta只能在同类型的datetime class之间,不能跨越 (比如date-datetime)
# timedelta 不支持time之间的运算,只支持date和datetime, 除非通过datetime实例中y,m,d均为同一个值(1)来实现
# 原因: 不考虑时区来比较时间是不安全的,所以计算需要通过datetime确定日期,或者确定timezone才能安全的对比
datetimeX1 = datetime.datetime(1,1,1, 17, 00, 00)
datetimeX2 = datetime.datetime(1,1,1, 16, 30, 59)
print(datetimeX1-datetimeX2)  # >>> 0:29:01
# 或者使用datetime.strptime() (在datetime.strptime()中会介绍)

A = datetime.timedelta(days=0.5, hours=0.5, seconds=100)  # 可以不用是整数,比如hour=0.5, 不受0-24/0-60限制
print(A)                  # >>> 12:31:40   # half a day + 30 min + 100 seconds

# timedelta 类属性
print(datetime.timedelta.min)  # >>> -999999999 days, 0:00:00         # 注意,最小值不是0,而是类似(-max)的概念
print(datetime.timedelta.max)  # >>> 999999999 days, 23:59:59.999999
# timedelta.resolution
# 不相等的timedelta对象之间的最小可能差值，timedelta(microseconds=1)


# timedelta 实例属性
A = datetime.timedelta(days=1, hours=2, seconds=100, microseconds=500)
print(A.days)             # >>> 1     # just day
print(A.seconds)          # >>> 7300  # 此处把hours也转换成秒(1天内的秒数)
print(A.microseconds)     # >>> 500   # just microseconds
# days属性可以取负值，另外两个属性都只能是正值

# timedelta 实例方法
print(A.total_seconds())  # >>> 93700.0005


print()
print('class datetime.date(year, month, day)')

# date 类属性
datetime.date.min # >>> 0001-01-01
datetime.date.max # >>> 9999-12-31
print(A.resolution) # >>> 0:00:00.000001

# date类方法
# date.today()
# 返回当前本地的日期
datetime.date(2017, 11, 9)  # 指定一个date
datetime.date.today()  # 返回当前本地的日期。这相当于(time.time())

# date.fromtimestamp(timestamp)
# 返回与POSIX时间戳对应的本地日期

# date.fromordinal(ordinal)
# 返回对应于公历序数的日期，其中第一年的一月一日为序数1

# date 实例属性
A = datetime.date(2017, 11, 8)
print(A.year)   # >>> 2017
print(A.month)  # >>> 11
print(A.day)    # >>> 8

# date间的运算,结合timedelta
A = datetime.date(2017, 11, 8)
B = datetime.date(2016, 11, 8)
C = B - A
D = A - B
print(type(C)) # >>>  <class 'datetime.timedelta'>
print(C) # >>> -365 days, 0:00:00
print(D) # >>>  365 days, 0:00:00
# 测试闰年 - 成功- 会计算出366天

# date 实例方法
A = datetime.date(2017, 8, 8)
A.replace(year=2016, month=7, day=7)
B = A.replace(year=2016, month=7, day=7)  # 依据关键字参数给出的新值，返回一个新的日期
print(A) # >>> 2017-08-08 # A不会因为replace被改变.
print(B) # >>> 2016-07-07 # 可以使用关键字(year, month, day),修改局部数据


A = datetime.date(2017, 8, 8)
print(A.timetuple())
# >>> time.struct_time(tm_year=2017, tm_mon=8, tm_mday=8, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=220, tm_isdst=-1)
# tm_wday - (0-6): Mon = 0, Sun = 6
# tm_yday: 这是今年的第几天(1月1号是第一天,不是第零天)

print(A.toordinal())   # >>> 736549  # 返回公历日期的序数，其中第1年的1月1日为第1天。
print(A.weekday())     # >>> 1  # same as tm_wday.(0-6): Mon = 0, Sun = 6
print(A.isoweekday())  # >>> 2  # 竟然不一样, (1-7): Mon = 1, Sun = 7
print(A.isocalendar()) # >>> (2017, 32, 2) 从1开始计算, 第2017年的第32周的第2天
print(A.isoformat())   # 2017-08-08 # YYYY-MM-DD
print(A.__str__())     # 对于日期d，str(d)等同于d.isoformat()
print(A.ctime())  # >>> Sat Jun  7 00:00:00 1986
print(A.strftime('%m/%d/%y'))           # >>> 08/08/17
print(A.strftime('%m/%d/%y %H:%M:%S'))  # >>> 08/08/17 00:00:00
print(A.__format__("%d/%m/%y"))  # same as above


print()
print('class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)')

# 基本就是date + time

# datetime类属性(基本与date相同)
# datetime.min  #　datetime(MINYEAR, 1, 1, tzinfo=None)
# datetime.max  # datetime(MAXYEAR, 12, 31, 23, 59, 59, 999999, tzinfo=None)
# datetime.resolution  # timedelta(microseconds=1)

# datetime 类方法
A = datetime.datetime(year=2017, month=3, day=15, hour=17, minute=15, second=30)
print(A)  # >>> 2017-03-15 17:15:30
# all (year, month, day, hour, minute, second, microsecond, tzinfo=None)

# datetime.today()
# 返回当前本地日期时间
print(datetime.datetime.today())   # >>> 2017-11-09 21:08:32.589043 精确到毫秒

# datetime.now(tz=None)
# 返回本地当前的日期和时间
print(datetime.datetime.now(tz=None))  # 若无tz,则基本等于today()

# datetime.utcnow()
# 返回当前UTC日期和时间
print(datetime.datetime.utcnow())

# datetime.fromtimestamp(timestamp, tz=None)
# 返回与POSIX时间戳对应的本地日期和时间

# datetime.utcfromtimestamp(timestamp)
# 返回与POSIX时间戳对应的UTC datetime

# datetime.fromordinal(ordinal)
# 返回对应于普通公历的序数的datetime，其中第1年的1月1日为序数1
print(datetime.datetime.fromordinal(365))  # >>> 0001-12-31 00:00:00
# 公元后xx天的日期    # 只接受天数作为参数

# datetime.combine(date, time)
# 返回一个新的datetime对象，其日期部分等于给定的date对象，其时间部分和tzinfo属性等于给定time对象

# datetime.strptime(date_string, format)
# 返回对应于date_string的datetime，根据format进行解析
sample1 = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(sample1)  # >>> datetime.datetime(2006, 11, 21, 16, 30)
sample2 = datetime.datetime.strptime("16:30:59", "%H:%M:%S")
print(sample2)  # >>> 1900-01-01 16:30:59  # default will give you a date 1900-01-01


# datetime 实例属性

A = datetime.datetime(year=2017, month=3, day=15, hour=17, minute=15, second=30, microsecond = 59)
print(A)  # >>> 2017-03-15 17:15:30.000059

print(A.strftime('%m/%d/%y %I:%M:%S %p'))  # >>> 03/16/17 05:15:30 PM
print(A.year)          # >>> 2017
print(A.month)         # >>> 3
print(A.day)           # >>> 16
print(A.hour)          # >>> 17
print(A.minute)        # >>> 15
print(A.second)        # >>> 30
print(A.microsecond)   # >>> 59
print(A.tzinfo)       # >>> None

# datetime 实例方法
# datetime.today()
# 返回当前本地日期时间

# datetime.now(tz=None)
# 返回本地当前的日期和时间

# datetime.utcnow()
# 返回当前UTC日期和时间

# datetime.fromtimestamp(timestamp, tz=None)
# 返回与POSIX时间戳对应的本地日期和时间

# datetime.utcfromtimestamp(timestamp)
# 返回与POSIX时间戳对应的UTC datetime

# datetime.fromordinal(ordinal)
# 返回对应于普通公历的序数的datetime，其中第1年的1月1日为序数1

# datetime.combine(date, time)
# 返回一个新的datetime对象，其日期部分等于给定的date对象，其时间部分和tzinfo属性等于给定time对象

# datetime.strptime(date_string, format)
# 返回对应于date_string的datetime，根据format进行解析

A = datetime.datetime(year=2017, month=3, day=15, hour=17, minute=15, second=30, microsecond=59)
print(A)  # >>> 2017-03-15 17:15:30.000059

# datetime.date()
# 返回具有相同年、月和日的date对象

# datetime.time()
# 返回具有相同小时、分钟、秒和微秒的time对象
print(A.time())  # >>> 17:15:30.000059

# datetime.timetz()
# 返回具有相同小时、分钟、秒、微秒和tzinfo属性的time对象

# datetime.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]])
# 返回具有相同属性的 datetime，但通过任何关键字参数指定新值的那些属性除外

# datetime.astimezone(tz=None)
# 返回带有新tzinfo属性tz的datetime对象，调整日期和时间数据使结果与self 的UTC时间相同，但为tz的本地时间

# datetime.utcoffset()
# 如果tzinfo为None，则返回None，否则返回self.tzinfo.utcoffset(self)；如果后者未返回None或表示小于一天的整数分钟的timedelta对象，则引发一个异常

# datetime.dst()
# 如果tzinfo为None，则返回None，否则返回self.tzinfo.dst(self)；如果后者未返回None或表示小于一天的整数分钟的timedelta对象，则引发一个异常

# datetime.tzname()
# 如果tzinfo为None，则返回None，否则返回self.tzinfo.tzname(self)；如果后者不返回None或字符串对象，则引发一个异常

# datetime.timetuple()
# 返回一个time.struct_time，类似time.localtime()的返回值
print(A.timetuple())
# >>> time.struct_time(tm_year=2017, tm_mon=3, tm_mday=15, tm_hour=17, tm_min=15, tm_sec=30, tm_wday=2, tm_yday=74, tm_isdst=-1)

# datetime.utctimetuple()
# 如果datetime实例d是naive的，它等同于d.timetuple()，但是无论d.dst()返回什么，tm_isdst都被强制设置为0。对于UTC时间DST始终不会生效

# datetime旗下.date()类的方法
# datetime.toordinal()
print(A.toordinal())      # >>> 736403  # 相距公元-天数,只返回天数
# datetime.timestamp()
# datetime.weekday()
# datetime.isoweekday()
# datetime.isocalendar()

# datetime.isoformat(sep='T')
# 可选参数sep（默认为'T'）是一个单字符分隔符，位于结果的日期和时间部分之间

# 其他类似date的实例方法
# datetime.__str__()
# datetime.ctime()
# datetime.strftime(format)
print(A.strftime('%m/%d/%y'))           # >>> 03/15/17
print(A.strftime('%m/%d/%Y %H:%M:%S'))  # >>> 03/15/2017 17:15:30

# datetime.__format__(format)


print()
print('class datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)')
# 所有参数都是可选的。tzinfo可以是None或tzinfo子类的实例
# time是哈希的,所以可以用作字典键

# time 类属性
# time.min
# 可表示的最早的time，time(0, 0, 0, 0)

# time.max
# 可表示的最晚的time，time(23, 59, 59, 999999)

# time.resolution
# 不相等的time对象之间的最小可能差，即timedelta(microseconds=1)

# time 实例属性(只读)
# time.hour         # 在range(24)之间。
# time.minute       #　在range(60)之间。
# time.second       # 在range(60)之间。
# time.microsecond  # 在range(1000000)之间。
# time.tzinfo       # 作为tzinfo参数传递给time构造函数的对象，如果没有传递则为None


# time 实例方法
# time.replace([hour[, minute[, second[, microsecond[, tzinfo]]]]])

# time.isoformat()
# 返回以ISO 8601 格式HH:MM:SS.mmmmmm表示间的字符串，如果self.microsecond为0，则以HH:MM:SS的格式

# time.__str__()
# 对于时间t，str(t)等同于t.isoformat()

# time.strftime(format)
# 返回一个表示time的字符串，由显式的格式字符串控制

# time.__format__(format)
# 与time.strftime()相同。这使得可以在使用str.format()时为time对象指定格式字符串

# time.utcoffset()
# 如果tzinfo为None，则返回None，否则返回self.tzinfo.utcoffset(None)；
# 如果后者未返回None或表示小于一天的整数分钟的timedelta对象，则引发一个异常

# time.dst()
# 如果tzinfo为None，则返回None，否则返回self.tzinfo.utcoffset(None)；
# 如果后者未返回None或表示小于一天的整数分钟的timedelta对象，则引发一个异常

# time.tzname()
# 如果tzinfo为None，则返回None，否则返回self.tzinfo.tzname(None)；
# 如果后者不返回None或字符串对象，则引发一个异常



print()
print('class datetime.tzinfo')
# 这是一个抽象的基类，意味着这个类不应该直接实例化
# 你需要派生一个具体的子类，并且（至少）提供你使用的datetime方法所需的标准tzinfo方法的实现
# datetime模块提供tzinfo的一个简单的具体子类timezone，它可以表示与UTC有固定偏移的时区，如UTC本身或北美EST和EDT
# tzinfo子类必须有一个可以无参数调用的__init__()方法

# tzinfo 类方法
# tzinfo的具体子类可能需要实现以下方法。需要哪些方法取决于对aware的datetime对象的使用

# tzinfo.utcoffset(dt)
# 返回本地时间与UTC的偏移量，以UTC东部分钟数为单位,如果本地时间在UTC的西边，它应该是负的。
# 注意，这是UTC的总偏移量
# 指定-1439到1439范围内的整数分钟（1440 = 24*60；偏移量必须小于一天）

# tzinfo.dst(dt)
# 如果DST信息未知，则返回夏令时（DST）调整（以UTC以东为单位），或者None。
# 如果DST不起作用，则返回timedelta(0)
# 如果DST有效，则将偏移返回为timedelta对象

# tzinfo.tzname(dt)
# 将与datetime对象dt对应的时区名称作为字符串返回。
# datetime模块没有定义有关字符串名称的内容，并且没有要求它有任何特别的意思。
# 例如，“GMT”、“UTC”、“-500”、“-5:00”、“EDT”、“US/Eastern”、“America/New York”都是有效的返回

# tzinfo.fromutc(dt)
# 这是从默认的datetime.astimezone()实现中调用的。
# 当从中调用时，dt.tzinfo为self，并且dt的日期和时间数据被视为表示UTC时间

# 举例说明
from datetime import tzinfo, timedelta, datetime
ZERO = timedelta(0)
HOUR = timedelta(hours=1)

class UTC(tzinfo):
    """UTC"""
    def utcoffset(self, dt):
        return ZERO
    def tzname(self, dt):
        return "UTC"
    def dst(self, dt):
        return ZERO

utc = UTC()
# A class building tzinfo objects for fixed-offset time zones.

# Note that FixedOffset(0, "UTC") is a different way to build a UTC tzinfo object.
class FixedOffset(tzinfo):
    """Fixed offset in minutes east from UTC."""

    def __init__(self, offset, name):
        self.__offset = timedelta(minutes=offset)
        self.__name = name

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return self.__name

    def dst(self, dt):
        return ZERO

# A class capturing the platform's idea of local time



print()
print('class datetime.timezone(offset, name=None)')

# timezone.utcoffset(dt)
# 返回构建timezone实例时指定的固定值。忽略dt参数。返回值是等于本地时间和UTC之差的timedelta实例

# timezone.tzname(dt)
# 返回在构建timezone实例时指定的固定值或字符串'UTCsHH:MM'，其中s是offset的符号，HH和MM分别是offset.hours和offset.minutes

# timezone.dst(dt)
# 始终返回None

# timezone.fromutc(dt)
# 返回dt + offset。dt参数必须是一个aware的datetime实例，其中tzinfo设置为self

# timezone 类属性：
# timezone.utc
# UTC时区，timezone(timedelta(0))

# Try out the timezone, and display time in different timezone

from datetime import datetime,timezone,timedelta

dtutc = datetime.utcnow()
print(dtutc)  # >>> 2018-01-17 21:41:10.514815  Straight UTC

dtutc = dtutc.replace(tzinfo=timezone.utc)
print(dtutc)  # >>> 2018-01-17 21:41:10.514815+00:00  Still UTC, but ready for convert

tzutc_8 = timezone(timedelta(hours=8))  # setup the time zone we want
dtbeijing = dtutc.astimezone(tzutc_8)
print(dtbeijing)


# Simplified version
print(datetime.utcnow().strftime('%m/%d/%y %H:%M:%S')) # >>> 01/17/18 21:51:15

tzutc_8 = timezone(timedelta(hours=8))  # GMT+8
DtBeijing = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(tzutc_8)
print(DtBeijing.strftime('%m/%d/%y %H:%M:%S'))         # >>> 01/18/18 05:50:35

tzutc_M5 = timezone(timedelta(hours=-5))  # GMT-5
DtNewyork = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(tzutc_M5)
print(DtNewyork.strftime('%m/%d/%y %H:%M:%S'))         # >>> 01/17/18 16:50:35
