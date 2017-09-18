a = 1
if a == 1:
    a = 2
elif a == 2:
    a = 3

print(a)

aliens = []
# Make 5 green aliens
for alien_number in range(5):
    new_alien = {'color': 'green'}
    aliens.append(new_alien)
print(aliens)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
print(aliens)

