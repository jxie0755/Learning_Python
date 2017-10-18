# mutation, alias, cloning

warm = ['red', 'yellow', 'orange']
hot = warm

print(warm)
print(hot)

hot.append('pink')
print(hot)
# change items in hot leads to change items in warm as well
print(warm)


cool = ['blue', 'green', 'grey']
chill = ['blue', 'green', 'grey']
# These two list looked like the same, but not the same item in the memory
cool[2] = 'blue'
print(chill)
# change items in chill does not change items in cool
print(cool)

# This will also create a copy
cool = ['blue', 'green', 'grey']
chill = cool[:]

# sort vs sorted
warm = ['red', 'yellow', 'orange']
sortedwarm = warm.sort()          # sort() returns None, and change the original list
reversedwarm = warm.reverse()     # same above

print(sortedwarm)
print(reversedwarm)

cool = ['blue', 'green', 'grey']
sortedcool = sorted(cool)       # sorted(list) returns a new list, but does not change the original list
reversedcool = reversed(cool)   # 

print(sortedcool)
print(reversedcool)




