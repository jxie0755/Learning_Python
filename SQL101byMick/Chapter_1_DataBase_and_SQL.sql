-- SQL 101 by Mick
-- Chapter 1 数据库和SQL


-- 将大量数据保存起来，通过计算机加工而成的可以进行高效访数据的数据集合称为数据库（Database， DB）
    -- 用来管理数据库的计算机系统称为数据库管理系统 (Database Management System， DBMS)
    -- 系统的使用者通常无法直接接触到数据库。因此，在使用系统的时候往往意识不到数据库的存在
    -- 文本文件/Excel 局限性
        -- 无法多人共享数据
        -- 无法提供操作大量数据所需的格式
        -- 实现读写自动化需要编程能力
        -- 实现读写自动化需要编程能力

-- DBMS的种类
    -- 层次数据库（Hierarchical Database， HDB）
        -- 把数据通过层次结构（树形结构）的方式表现出来
        -- 曾经是数据库的主流
    -- 关系数据库（Relational Database， RDB）
        -- 现在应用最广泛的数据库
        -- 由行和列组成的二维表来管理数据，所以简单易懂
        -- 使用专门的 SQL（StructuredQuery Language，结构化查询语言）对数据进行操作
            -- Oracle Database：甲骨文公司的RDBMS
            -- SQL Server：微软公司的RDBMS
            -- DB2：IBM公司的RDBMS
            -- PostgreSQL： 开源的RDBMS
            -- MySQL：开源的RDBMS
    -- 面向对象数据库（Object Oriented Database， OODB
        -- 把数据以及对数据的操作集合起来以对象为单位进行管理
    -- XML数据库（XML Database， XMLDB）
        -- 在网络上进行交互的数据的形式逐渐普及起来
        -- 对 XML 形式的大量数据进行高速处理
    -- 键值存储系统（Key-Value Store， KVS）
        -- 单纯用来保存查询所使用的主键（Key）和值（Value）的组合的数据库
        -- 把它想象成关联数组或者散列（hash）
        -- 被应用到 Google 等需要对大量数据进行超高速查询的 Web 服务当中


-- RDBMS 常见结构
    -- 客户端 - 服务器 - 数据库 结构
        -- 客户端发送SQL语句给服务器
        -- 服务器处理语句，写入或读取数据
        -- 返回给客户端
            -- 根据SQL语句的内容返回的数据同样必须是二维表的形式

-- 表的结构
    -- 垂直方向称为 列 / 字段， 列有列名
    -- 水平方向称为 行 / 记录， 一行则是一条数据
        -- 关系数据库必须以行为单位进行数据读写
    -- 行与列的交叉叫单元格, 一个单元格只能输入一个数据

