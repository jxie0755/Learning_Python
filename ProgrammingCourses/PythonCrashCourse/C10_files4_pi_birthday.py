# 使用读取的文件内容
# 仍然基于pi_digits.txt做演示 (假设文件有100万位的pi数据)

filename = "M_M_pi_million_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()

# 开始进行使用
pi_string = ""
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form of mmddyy: ") # 设立input生日信息

if birthday in pi_string:
    print("your birthday information is included in 1 million digits of pi")
else:
    print("your birthday information is not found in pi")
