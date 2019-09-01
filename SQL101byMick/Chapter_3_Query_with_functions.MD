# SQL 101 by Mick #
## Chapter 3 对表进行聚合查询 ##


### 聚合函数 ###

- 用于汇总的函数成为聚合函数或者聚集函数
- 5个常用函数
    - `COUNT`: 计算行数
    - `SUM`: 求和
    - `AVG`: 求平均值
    - `MAX`: 最大值
    - `MIN`: 最小值

实例: 计算Product列表的行数
```
SELECT COUNT(*)
FROM Product;
```
- `COUNT(*)`统计所有行数
- `COUNT(purchase_price)`统计改列非空行的行数



