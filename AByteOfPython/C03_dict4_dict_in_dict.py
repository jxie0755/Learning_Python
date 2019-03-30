# DICT IN DICT
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print('\nUsername:', username)
    full_name = user_info['first'] + ' ' + user_info['last']   # 不要再设定变量的时候安排大小写,安排在最后print就可以
    location = user_info['location']

    print('\tFull name:', full_name.title())
    print('\tLocation:', location.title())
