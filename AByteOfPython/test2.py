# Make an empty list to store aliens
aliens = []

# Make 30 green aliens
for alien_number in range(5):   # 不需要使用(0, 30), 默认从0开始到29
    # 需要注意的就是这里的alien_number跟后面的new alien其实没什么关系,只不过是限定了一个做30个alien的范围. 新造出来的alien不会因此就被编号.
    new_alien = {'color': 'green', 'size': 5, 'speed': 'slow'}
    new_alien2 = {'color': 'yellow', 'size': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    aliens.append(new_alien2)

# Show the first 5 aliens:
for alien in aliens[:]:
    print(alien)
print("...")

# Show how many aliens have been created.
print('Total number of aliens:', len(aliens))

# 对于以上alien,再进行更细致的修改
# 将前三个改成yellow, size 10, medium speed.
for alien in aliens[:]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
for alien in aliens[:5]:
    print(alien)
print("...")
