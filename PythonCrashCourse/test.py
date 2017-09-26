# 写入一个list到write_list.txt中:

list = ['1. Denis', '2. Cindy', '3. Adrienne']
with open('write_list.txt', 'w') as f_obj:
    f_obj.write(' '.join(list)) # ''控制链接方式


# 写入tuple到write_tuple.txt中:

tuple = ('Denis', 'Cindy', 'Adrienne')
with open('write_tuple.txt', 'w') as f_obj:
    f_obj.write('\n'.join(tuple))

# 写入dict到write_dict.txt中:
import json
dict = {'Denis': 1, 'Cindy': 2, 'Adrienne': 3}
with open('write_dict.txt', 'w') as f_obj:
    for k, v in dict.items():
        f_obj.write(str(k) + ': ' + str(v) + '\n')