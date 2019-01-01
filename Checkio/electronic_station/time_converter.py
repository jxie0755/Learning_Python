# You are the modern man who prefers the 24-hour time format. But the 12-hour format is used in some places.
# Your task is to convert the time from the 12-h format into 24-h by following the next rules:
# the output format should be 'hh:mm'

# Input: Time in a 12-hour format (as a string).
# Output: Time in a 24-hour format (as a string).


def time_converter(time):
    hr_str = time.split(':')[0]
    min_str = time.split(':')[1].split(' ')[0]
    AMPM = time.split(':')[1].split(' ')[1]

    if time == '12:00 a.m.':
        return '00:00'
    if AMPM == 'a.m.':
        hr_str = '0' + hr_str
    elif AMPM == 'p.m.' and hr_str != '12':
        hr_str = str((int(hr_str) + 12))
        if hr_str == '24':
            hr_str = '00'
    else:
        hr_str = '12'

    return hr_str + ':' + min_str

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")

