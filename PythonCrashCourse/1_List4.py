# 将一个list中所有item都变成大写/小写,并且反向

list_D = ['jack', 'Bob', 'frank', 'Benji', 'cathy', 'illy', 'ben', 'hank', 'billy', 'Adrienne']
list_D = [i.upper() for i in list_D]
list_D.reverse()
print(list_D)

# 此处使用for in loop在一个list中,使得list能够包括原所有的item
