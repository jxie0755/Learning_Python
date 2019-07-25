# Sams Teach yourself SQL in 10 Mins
# Chapter 2 Search Data


USE sams_teach_sql;

# The SELECT Stament

# 为了使用 SELECT 检索表数据，必须至少给出两条信息
# 想选择什么，
# 以及从什么地方选择


# 检索单个列 (未必排序了)
SELECT prod_name
FROM products;

# 检索多个列
SELECT prod_id, prod_name, prod_price
FROM products;

# 检索所有列
# 与python相同, *表示所有内容
SELECT *
FROM customers;
# 一般而言，除非你确实需要表中的每一列，否则最好别使用*通配
# 建议慎用, 会降低性能, 只找需要的内容


