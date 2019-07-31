# Sams Teach yourself SQL in 10 Mins
# Chapter 3 Sorting Retried Data

USE sams_teach_sql;

# 子句概念(clause)
# SQL 语句由子句构成
# 有些子句是必需的
# 有些则是可选的


# Order By 子句
SELECT prod_name
FROM products
ORDER BY prod_name;
# 必须是最后一句
# 按照prod_name排序


# 按多个列排序
SELECT prod_id, prod_price, prod_name
FROM products
ORDER BY prod_price, prod_name;
# 也就是先按价格排序, 然后相同价格的内容再按名称排子顺序
