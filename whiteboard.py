from TextWash.zhonTranslate import CNwash

# CNwash(r"D:\Documents\GitHub\Learning_SQL\SQL101byMick\Chatper_5_Complex_Query.md")


import os
# for sub in os.listdir(r"C:\Users\jxie0\Documents"):
#     print(sub)

for sub in os.walk(r"C:\Users\jxie0\Documents"):
    print(sub)

