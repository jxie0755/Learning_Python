def checkio(time_string):
    # process time_string
    str_list = [i.zfill(2) for i in time_string.split(':')]
    translation = {0: '....', 1: '...-', 2: '..-.', 3: '..--', 4: '.-..',
                   5: '.-.-', 6: '.--.', 7: '.---', 8: '-...', 9: '-..-'
                   }

    r = ''
    for i in str_list:
        r += translation[int(i[0])] + ' '
        r += translation[int(i[1])] + ' '
    return r[2:4] + r[4:10] + ': ' + r[11:14] + r[14:20] + ': ' + r[21:24] + r[24:29]


# also check
def checkio3(ts):
    ts = ''.join('%02d' % int(a) for a in ts.split(':'))
    bts = ['{:0{dig}b}'.format(int(a), dig=b) for a, b in zip(ts, [2, 4, 3, 4, 3, 4])]
    bts = [c.replace('0', '.').replace('1', '-') for c in bts]
    return '{} {} : {} {} : {} {}'.format(*bts)


assert checkio3("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
assert checkio3("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
assert checkio3("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
assert checkio3("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
print('done')
