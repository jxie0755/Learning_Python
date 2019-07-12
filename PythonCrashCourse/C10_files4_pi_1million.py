# 使用读取的文件内容
# 仍然基于pi_digits.txt做演示 (假设文件有100万位的pi数据)

filename = "M_M_pi_million_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()

# 开始进行使用
pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string[:22] + "...") # 限制打印到前20个数字
print("length is", len(pi_string), "digits") # list长度仍然是全长
