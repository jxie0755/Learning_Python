# Dict in list

# Make an empty list to store aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):   # 不需要使用(0, 30), 默认从0开始到29
    # 需要注意的就是这里的alien_number跟后面的new alien其实没什么关系,只不过是限定了一个做30个alien的范围. 新造出来的alien不会因此就被编号.
    new_alien = {'color': 'green', 'size': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print('Total number of aliens:', len(aliens))

# 对于以上alien,再进行更细致的修改
# 将前三个改成yellow, size 10, medium speed.
for i in aliens[:3]:        # 订位前三个
    i['color'] = 'yellow'
    i['size'] = 10
    i['speed'] = 'medium'   # 这里要注意,不能再用new_alien['color']
    # 当初new_alien被添加到aliens的list中后,失去了身份,在遍历过程中,list中的元素都为临时设定的变量而已,这里直接用i来表达都可以.

for alien in aliens[:5]:
    print(alien)
print("...")


for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[:5]:
    print(alien)
print("...")
