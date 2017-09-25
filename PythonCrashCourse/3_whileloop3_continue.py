# Example to use continue

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue            # 使用continue来忽略偶数, 跳过print命令,回到loop开头
    print(current_number)   # 注意这个print的缩进位置
