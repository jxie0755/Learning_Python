# SQL 101 by Mick #
## Chapter 2 查询基础 ##


### SELECT 语句基础 ###

#### 列的查询 ####
- 从表中选取数据使用`SELECT`语句
- 通过`SELECT`语句查询并选取必要数据的过程叫匹配查询(Query)
- `SELECT`语句石SQL中使用最多的最基本的语句

`SELECT`基本用法:
```sql
SELECT <列名>, ...
FROM <表名>;
```
- 两个子句(clause)
    - `SLECT` 列举列的名称
    - `FROM`  指定表的名称

实例:
```
SELECT product_id, product_name, purchase_price
    FROM Product;
```
- 用逗号`,`分隔多列
- 列的顺序和`SELECT`子句中顺序相同(不一定,但可以额外设置)
- 列中的数据没有固定的顺序

#### 查询所有列 ####

```sql
SELECT *
FROM <表名>
```
- `*`号代表所有
- 使用`*`就没没法设定顺序? 此时按照`CREATE TABLE`语句排序


**注意:**
- SQL可以随意使用换行
- 但是不要插入空行

#### 为列设定别名 ####
```
SELECT product_id     AS id,
       product_name   AS name,
       purchase_price AS "进货价格"
FROM Product;
```
- 这样在显示出来的table中,列名就被换成了别名
- 使用中文时注意使用双引号`"中文"`
    - Jetbrains的IDE貌似不需要


#### 常数的查询 ####

```
SELECT '商品' AS string, 38 AS number, '2009-02-24' AS date,
        product_id, product_name
FROM Product;
```
- 这样使用常数时, 新增了`string`, `number`和`date`三个列
- 每个列都全部填满了语句中的常数


#### 删除重复行 ####
```
SELECT DISTINCT purchase_price
FROM Product;
```
- 这样就会显示无重复的列数据
- `NULL`也会被视为一类数据

如果出现多个列
```
SELECT DISTINCT product_type, regist_date
FROM product;
```
- `DISTINCT` 必须用在第一个列名之前
- 这里`product_type`出现重复, 因为他们`regist_date`不同个
    - 所以`DISTINCT`多个类, 只要有一列不同, 就算不同
    - 也就是只有两行中所有列的数据都相同才会被合并


#### WHERE 语句 ####
通过使用`WHERE`添加选择条件
```sql
SELECT <列名>, ...
FROM <表名>
WHERE <条件表达式>;
```

实例: 选取品类为`衣服`的记录
```
SELECT product_name, product_type
FROM Product
WHERE product_type = '衣服';
```

```
SELECT product_name
FROM Product
WHERE product_type = '衣服';
```

实例2: 选取价格<=1000的商品
```
SELECT product_name, product_type, sale_price,
FROM Product
WHERE sale_price <= 1000;
```
- 未必筛选的信息需要被`SELECT`
- `WHERE`必须在`FROM`之后


### 算数运算符和比较运算符 ###



### 逻辑运算符 ###
