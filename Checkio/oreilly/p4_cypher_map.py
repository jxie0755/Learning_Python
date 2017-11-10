# Write a module that enables the robots to easily recall their passwords through codes when they return home.
# The cipher grille and the ciphered password are represented as an array (tuple) of strings.
# Input: A cipher grille and a ciphered password as a tuples of strings.
# Output: The password as a string.

def recall_password(cipher_grille, ciphered_password):
    
    # define a function to express the password from the current grill
    def decrypt(cipher_grille, ciphered_password):
        sn = ''
        coor1 = ''.join((map(lambda x: str(x) * cipher_grille[x].count('X'), list(range(4)))))
        coor2 = ''
        for i in cipher_grille:
            for n in range(4):
                if i[n] == 'X':
                    coor2 += str(n)
        for c in range(0,4):
            sn += ciphered_password[int(coor1[c])][int(coor2[c])]
        return sn
    
    # define a function to rotate the cipher_grille 90 degree clockwise
    def rotate(cipher_grille):
        def new(n):
            new_line = ''
            for i in range(4):
                new_line += cipher_grille[i][n]
            return new_line[::-1]
        new_grille = list(map(new, list(range(4))))    
        return new_grille
    
    # add 4 runs of decrypt() together as the final password
    password = ''
    for i in range(4):
        r = decrypt(cipher_grille, ciphered_password)
        cipher_grille = rotate(cipher_grille)
        password += r
    
    return password

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'
    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
