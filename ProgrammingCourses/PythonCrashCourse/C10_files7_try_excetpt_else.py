# 设置一个循环,以q退出
# 目的是计算两数相除
# 用try...except...else来解决异常

while True:

    first_number = input("\nFirst number: ")
    if first_number == "q":
        break

    second_number = input("Second number: ")
    if second_number == "q":
        break

    try: # try必须只包含可能出错的代码,不要放太多内容
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can\"t divide by zero.')
    else: # 依赖try代码成功后,执行的代码都放在else
        print(answer)

    # 这样也可以,但是不好.
    try:
        answer = int(first_number) / int(second_number)
        print(answer)
    except ZeroDivisionError:
        print("You can\"t divide by zero.')

# 处理FileNotFoundError 异常

filename = "D_alice.txt"

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry the file " + "\""+ filename + "\""+ " was not found."
    print(msg)
