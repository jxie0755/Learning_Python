# list of list of list

warm = ['yellow', 'orange']
hot = ['red']
brightcolors = [warm]

brightcolors.append(hot)
print(brightcolors)

hot.append('pink')
print(hot)
print(brightcolors)
del warm[0]
print(brightcolors)
