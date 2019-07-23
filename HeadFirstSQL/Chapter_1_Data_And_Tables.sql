# Head First SQL

# Chapter 1
# Data and Tables: A place for everything

# 数据库是保存表和其他相关SQL结构的容器
# 在数据库查找信息的行为叫Query
# 数据库由表构成, 表则包含数据
# 表由行和列构成
# 列是储存在表中的一块数据, 一项分类信息
# 行是一组能够描述某个事物的列的集合
# 数据库中的所有表应该能以某种方式互相关联
# 数据库和表的名称不一定要大写


# 接受命令
# SQL关系型数据库管理系统 Relational Database Management System (RDBMS)


# 创建数据库
CREATE DATABASE gregs_list;
# 必须以分号结束
# 若重复创建则会收到错误信息:
# [HY000][1007] Can't create database 'gregs_list'; database exists

# 现在要告诉RDBMS进入/使用被建造出来的数据库
USE gregs_list;
# 现在开始做的每件事都在gregs_list数据库中进行

# 命名建议
# SQL本身不区分大小写, 但是建议命令用大写
# 名称不能包含空格, 可以用_替代空格
# 没有固定命名规则, 但是注意避免首字母大写
# [']符号被保留了, 有特殊作用, 建议省略


# 设定表 (同理也是不能重复创建)
CREATE TABLE doughtnut_list
(
    doughnut_name VARCHAR(10), # 可变字符,最多10个字符
    doughnut_type VARCHAR(6)
);


CREATE TABLE my_contacts
(
    last_name  VARCHAR(30),
    first_name VARCHAR(20),
    email      VARCHAR(50),
    gender     CHAR(1),
    birthday   DATE,
    profession VARCHAR(50),
    location   VARCHAR(50),
    status     VARCHAR(20),
    interest   VARCHAR(100),
    seeking    VARCHAR(100)
);
# 注意! 不能随意追加列! 如果要追加, 可以删了旧表重建
# TODO 未来会有不破坏数据而改变表的方式


# 查看表 Describe
DESC my_contacts;

# 删除表 (删除表和表内的所有数据, 务必小心, 这里无法挽回)
# DROP TABLE my_contacts;


# 插入值
INSERT INTO my_contacts
(last_name, first_name, email, gender, birthday, profession, location, status, interest, seeking)
VALUES # 注意换行 (注意, VALUE和VALUES 都是可以的, 作用完全相同
       ('Anderson', 'Jillian', 'jill_anderson@breakneckpizza.com', 'F', '1980-09-05', 'TechnicalWriter',
        'Palo Alto, CA', 'Single', 'Kayaking, Reptiles', 'Relationship, Friends');
# 数据值得顺序必须和列的顺序完全一样!


# 其他Insert变体
# 改变列顺序
INSERT INTO my_contacts # 交换first和last name
(first_name, last_name, email, gender, birthday, profession, location, status, interest, seeking)
VALUES ('Gillian', 'Banderson', 'gill_banderson@breakneckpizza.com', 'F', '1980-09-05', 'TechnicalWriter',
        'Palo Alto, CA', 'Single', 'Kayaking, Reptiles', 'Relationship, Friends');

# 省略列名
INSERT INTO my_contacts # 交换first和last name
VALUES ('Baanderson', 'GGillian', 'ggill_baanderson@breakneckpizza.com', 'F', '1980-09-05', 'TechnicalWriter',
        'Palo Alto, CA', 'Single', 'Kayaking, Reptiles', 'Relationship, Friends');

# 选择性省略一部分列
INSERT INTO my_contacts
    (first_name, email, profession, location)
VALUES ('Pat', 'patpost@breakingpizza.com', 'Postal Worker', 'Princeton, NJ');
