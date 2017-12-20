# Input: Two arguments. A string to be hashed and a hash algorithm as a string (unicode utf8).
# Output: Hexadecimal hash for for input string using given algorithm as a string.

import hashlib

def checkio(hashed_string, algorithm):
    if algorithm == 'md5':
        return hashlib.md5(str.encode(hashed_string)).hexdigest()
    if algorithm == 'sha224':
        return hashlib.sha224(str.encode(hashed_string)).hexdigest()
    if algorithm == 'sha256':
        return hashlib.sha256(str.encode(hashed_string)).hexdigest()
    if algorithm == 'sha384':
        return hashlib.sha384(str.encode(hashed_string)).hexdigest()
    if algorithm == 'sha512':
        return hashlib.sha512(str.encode(hashed_string)).hexdigest()
    if algorithm == 'sha1':
        return hashlib.sha1(str.encode(hashed_string)).hexdigest()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('welcome', 'md5') == '40be4e59b9a2a2b5dffb918c0e86b3d7'
    assert checkio('happy spam', 'sha224') == '6e9dc3e01d57f1598c2b40ce59fc3527e698c77b15d0840ae96a8b5e'
    print('done')


def checkio2(hashed_string, algorithm):
    return eval("hashlib." + algorithm +
    "((hashed_string).encode('utf-8')).hexdigest()")

def checkio3(string, algorithm):
    h = hashlib.new(algorithm,string.encode('utf-8'))
    return h.hexdigest()

def checkio4(hashed_string, algorithm):
    return (getattr(hashlib, algorithm)(hashed_string.encode('utf8'))).hexdigest()


