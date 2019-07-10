# 简略学习SQL知识, 基于廖雪峰SQL简单教程
# https://www.liaoxuefeng.com/wiki/1177760294764384



# 么是SQL？
    # 简单地说，SQL就是访问和处理关系数据库的计算机标准语言。
    # 也就是说，无论用什么编程语言（Java、Python、C++……）编写程序，只要涉及到操作关系数据库
# NoSQL数据库
    # 也就是非SQL的数据库，包括MongoDB、Cassandra、Dynamo等等


# 要保存一个班级所有学生的信息，可以向文件中写入一个CSV文件
# id,name,gender,score
# 1,小明,M,90
# 2,小红,F,95
# 3,小军,M,88
# 4,小丽,F,88

# 但是，随着应用程序的功能越来越复杂，数据量越来越大，如何管理这些数据就成了大问题：
    # 读写文件并解析出数据需要大量重复代码
    # 从成千上万的数据中快速查询出指定数据需要复杂的逻辑

# 如果每个应用程序都各自写自己的读写数据的代码
    # 一方面效率低，容易出错
    # 另一方面，每个应用程序访问数据的接口都不相同，数据难以复用


# 数据库作为一种专门管理数据的软件就出现了。
    # 应用程序不需要自己管理数据，而是通过数据库软件提供的接口来读写数据。
    # 至于数据本身如何存储到文件，那是数据库软件的事情，应用程序自己并不关心
    # application和database互为读写


# 数据模型
# 数据库按照数据结构来组织、存储和管理数据，实际上，数据库一共有三种模型：
    # 层次模型
        # 类似二叉树
    # 网状模型
        # 相互交错连接
    # 关系模型
        # 类似excel表格
        # 任何数据都可以通过行号+列号来唯一确定

# 随着时间的推移和市场竞争，最终，基于关系模型的关系数据库获得了绝对市场份额。
    # 因为相比层次模型和网状模型，关系模型理解和使用起来最简单。



# 数据类型
# 对于一个关系表，除了定义每一列的名称外，还需要定义每一列的数据类型。关系数据库支持的标准数据类型包括数值、字符串、时间等：

# 名称            类型	               说明
# INT            整型           4字节整数类型，范围约+/-21亿
# BIGINT         长整型          8字节整数类型，范围约+/-922亿亿

# REAL           浮点型          4字节浮点数，范围约+/-1038
# DOUBLE         浮点型          8字节浮点数，范围约+/-10308
# DECIMAL(M,N)   高精度小数      由用户指定精度的小数，例如，DECIMAL(20,10)表示一共20位，其中小数10位，通常用于财务计算

# CHAR(N)        定长字符串      存储指定长度的字符串，例如，CHAR(100)总是存储100个字符的字符串
# VARCHAR(N)     变长字符串      存储可变长度的字符串，例如，VARCHAR(100)可以存储0~100个字符的字符串

# BOOLEAN        布尔类型        存储True或者False

# DATE           日期类型        存储日期，例如，2018-06-22
# TIME           时间类型        存储时间，例如，12:20:59
# DATETIME       日期和时间类型   存储日期+时间，例如，2018-06-22 12:20:59


# 上面的表中列举了最常用的数据类型。很多数据类型还有别名
    # 例如，REAL又可以写成FLOAT(24)。
# 还有一些不常用的数据类型
    # 例如，TINYINT（范围在0~255）。
    # 各数据库厂商还会支持特定的数据类型，例如JSON


# 主流关系数据库
# 目前，主流的关系数据库主要分为以下几类：
    # 商用数据库，例如：Oracle，SQL Server，DB2等；
    # 开源数据库，例如：MySQL，PostgreSQL等；
    # 桌面数据库，以微软Access为代表，适合桌面应用程序使用；
    # 嵌入式数据库，以Sqlite为代表，适合手机应用和桌面程序。


# SQL (Structured Query Language)
    # SQL是结构化查询语言的缩写，用来访问和操作数据库系统。
    # SQL语句既可以查询数据库中的数据，也可以添加、更新和删除数据库中的数据，还可以对数据库进行管理和维护操作。
    # 不同的数据库，都支持SQL，
    # 这样，我们通过学习SQL这一种语言，就可以操作各种不同的数据库。

    # 不幸地是，各个不同的数据库对标准的SQL支持不太一致。
    # 并且，大部分数据库都在标准的SQL上做了扩展。
        # 也就是说，如果只使用标准SQL，理论上所有数据库都可以支持，
        # 但如果使用某个特定数据库的扩展SQL，换一个数据库就不能执行了
    # 各个数据库支持的各自扩展的功能，通常我们把它们称之为“方言”


# SQL语言定义了这么几种操作数据库的能力：
    # DDL：Data Definition Language
        # DDL允许用户定义数据，也就是创建表、删除表、修改表结构这些操作。
        # 通常，DDL由数据库管理员执行。
    # DML：Data Manipulation Language
        # DML为用户提供添加、删除、更新数据的能力，这些是应用程序对数据库的日常操作。
    # DQL：Data Query Language
        # DQL允许用户查询数据，这也是通常最频繁的数据库日常操作。

# 语法特点
    # SQL语言关键字不区分大小写！！！
    # 但是，针对不同的数据库，对于表名和列名，有的数据库区分大小写，有的数据库不区分大小写。
    # 同一个数据库，有的在Linux上区分大小写，有的在Windows上不区分大小写。
    # 所以，本教程约定：SQL关键字总是大写，以示突出，表名和列名均使用小写。






