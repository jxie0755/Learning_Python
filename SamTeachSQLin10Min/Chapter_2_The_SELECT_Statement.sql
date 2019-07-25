# Sams Teach yourself SQL in 10 Mins
# Chapter 2 Search Data


USE sams_teach_sql;

# The SELECT Stament

# 为了使用 SELECT 检索表数据，必须至少给出两条信息
# 想选择什么，
# 以及从什么地方选择

# 检索全部内容
SELECT * # 与python相同, *表示所有内容
FROM customers;


# 检索单个列
SELECT prod_name
FROM products;

