# Input: A number as an integer. The keyword argument "base" as an integer, default 1000. The keyword argument "decimals" as an integer, default 0. The keyword argument "powers" as a list of string, default ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y'].
# Output: The converted number as a string.

def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    prefix = ''
    zn = ''
    if number < 0:
        zn = "-"
    number = abs(number)
    answer = number

    for i, power in enumerate(powers):
        if number // (base ** i) > 0:
            answer = number // (base ** i)
            prefix = powers[i]
    if decimals:
        i = powers.index(prefix)
        frac = round(number / (base ** i), decimals)
        a_lst = str(frac).split(".")
        answer = a_lst[0] + "." + a_lst[1]
    return zn + str(answer) + prefix + suffix


# assert friendly_number(102) == '102', '102'
# assert friendly_number(10240) == '10k', '10k'
# assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
# assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
# assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'

print(friendly_number(102))
print(friendly_number(10240))
print(friendly_number(12341234, decimals=1))
print(friendly_number(12461, decimals=1))
