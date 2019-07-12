# Learn psutil


# 用Python来编写脚本简化日常的运维工作是Python的一个重要用途。
# 在Linux下，有许多系统命令可以让我们时刻监控系统运行的状态，如ps，top，free等等。
# 要获取这些系统信息，Python可以通过subprocess模块调用并获取结果。
# 但这样做显得很麻烦，尤其是要写很多解析代码。

# 在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。
    # 顾名思义，psutil = process and system utilities，
    # 它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，
    # 支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块


import psutil

print(psutil.cpu_count(logical=False)) # >>> 6
print(psutil.cpu_count())              # >>> 12  (6核12线程)

print(psutil.cpu_times())
# >>>  scputimes(user=39662.21875,
        # system=35107.00000000186,
        # idle=9924613.437499998,
        # interrupt=2070.140625,
        # dpc=2125.78125)


# 再实现类似top命令的CPU使用率，每秒刷新一次，累计10次
# for x in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))
# [4.7, 4.7, 4.7, 1.6, 4.7, 3.1, 14.1, 3.1, 4.7, 4.7, 3.1, 15.6]
# [6.2, 0.0, 1.6, 0.0, 0.0, 0.0, 4.7, 1.6, 0.0, 0.0, 3.1, 0.0]
# [4.7, 0.0, 0.0, 0.0, 1.6, 0.0, 7.8, 0.0, 0.0, 3.1, 1.6, 1.6]
# [1.6, 0.0, 0.0, 1.6, 3.1, 0.0, 4.7, 3.1, 0.0, 3.1, 0.0, 1.6]
# [3.1, 0.0, 3.1, 1.6, 0.0, 0.0, 3.1, 1.6, 0.0, 0.0, 0.0, 1.6]
# [7.7, 0.0, 3.1, 6.2, 1.6, 0.0, 1.6, 1.6, 0.0, 3.1, 0.0, 0.0]
# [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.6, 1.6, 0.0, 0.0, 0.0, 0.0]
# [3.1, 0.0, 3.1, 0.0, 3.1, 0.0, 1.6, 1.6, 0.0, 1.6, 0.0, 1.6]
# [6.2, 1.6, 3.1, 1.6, 3.1, 1.6, 6.2, 3.1, 3.1, 3.1, 3.1, 1.6]
# [18.2, 3.1, 7.8, 3.1, 6.2, 1.6, 12.5, 3.1, 1.6, 12.5, 3.1, 9.4]
# 统计12个线程的占用情况一共10秒



# 使用psutil获取物理内存和交换内存信息
print()
print(psutil.virtual_memory())
# svmem(total=34286256128, available=20262420480, percent=40.9, used=14023835648, free=20262420480)
# 总内存 34G, 还有20G, 占用40%, 用了14G
print(psutil.swap_memory())
# sswap(total=39386529792, used=20041703424, free=19344826368, percent=50.9, sin=0, sout=0)
# 而交换区大小是1073741824 = 40 GB



# 可以通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息
print()
print(psutil.disk_partitions()) # 磁盘分区信息
# [sdiskpart(device="C:\\", mountpoint="C:\\", fstype="NTFS", opts="rw,fixed"),
# sdiskpart(device="D:\\", mountpoint="D:\\", fstype="NTFS", opts="rw,fixed"),
# sdiskpart(device="E:\\", mountpoint="E:\\", fstype="NTFS", opts="rw,fixed"),
# sdiskpart(device="F:\\", mountpoint="F:\\", fstype="NTFS", opts="rw,fixed")]

print(psutil.disk_usage("/")) # 磁盘使用情况
# sdiskusage(total=500090007552, used=204505022464, free=295584985088, percent=40.9)

print(psutil.disk_io_counters()) # 磁盘IO
# sdiskio(
# read_count=4929858, write_count=8759548,
# read_bytes=321037917184, write_bytes=347494014976,
# read_time=4129, write_time=4759)


# psutil可以获取网络接口和网络连接信息
print()
print(psutil.net_io_counters()) # 获取网络读写字节／包的个数
# snetio(bytes_sent=68468541570, bytes_recv=121054712924,
# packets_sent=112391551, packets_recv=133056843,
# errin=0, errout=15, dropin=0, dropout=0)
print()
print(psutil.net_if_addrs() )# 获取网络接口信息
print()
print(psutil.net_if_stats()) # 获取网络接口状态

# 要获取当前网络连接信息，使用net_connections()
print()
print(psutil.net_connections())


# 通过psutil可以获取到所有进程的详细信息
print()

print(psutil.pids()) # 所有进程ID
p = psutil.Process(7816) # 获取指定进程ID=3776，其实就是当前Python交互环境 (可在task manager details tab里面核实)

print(p.name())  # 进程名称
# >>> pycharm64.exe

print(p.exe())   # 进程exe路径
# >>> C:\Program Files\JetBrains\PyCharm 2018.3.3\bin\pycharm64.exe

print(p.cwd())     # 进程工作目录
# >>>  C:\Program Files\JetBrains\PyCharm 2018.3.3\bin

print(p.cmdline()) # 进程启动的命令行
# >>> ["C:\\Program Files\\JetBrains\\PyCharm 2018.3.3\\bin\\pycharm64.exe"]

print(p.ppid())   # 父进程ID
# >>> 33168

print(p.parent())   # 父进程
# >>> None

print(p.children())  # 子进程列表
# >>>  [psutil.Process(pid=8744, name="fsnotifier64.exe", started="14:56:08"), psutil.Process(pid=15096, name="SGTool.exe", started="15:16:37"), psutil.Process(pid=29136, name="python.exe", started="15:19:33")]

print(p.status())  # 进程状态
# >>>  running

print(p.username())  # 进程用户名
# >>> XJ-SERVER\jxie0755

print(p.create_time()) # 进程创建时间
# >>> 1554144965.0

# print(p.terminal()) # 进程终端
# print(cpu_times())  # 进程使用的CPU时间

print(p.memory_info()) # 进程使用的内存
# >>> pmem(rss=1848827904, vms=2961432576, num_page_faults=1351431, peak_wset=1899991040, wset=1848827904, peak_paged_pool=885320, paged_pool=884184, peak_nonpaged_pool=120164, nonpaged_pool=95080, pagefile=2961432576, peak_pagefile=3017007104, private=2961432576)
