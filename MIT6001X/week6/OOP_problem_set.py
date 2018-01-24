# This assignment will deal with a well-known (though not very secure) encryption method called the Caesar cipher.
# Some vocabulary to get you started on this problem

# Encryption - the process of obscuring or encoding messages to make them unreadable until they are decrypted
# Decryption - making encrypted messages readable again by decoding them
# Cipher - algorithm for performing encryption and decryption
# Plaintext - the original message
# Ciphertext - the encrypted message.

# ps6.py - a file containing three classes that you will have to implement.
# words.txt - a file containing valid English words (should be in the same folder as your ps6.py file).
# story.txt - a file containing an encrypted message that you will have to decode (should be in the same folder as your ps6.py file).

import string


class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        # self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        k_low = string.ascii_lowercase
        k_up = string.ascii_uppercase
        v_low = k_low[shift:] + k_low[:shift]
        v_up = k_up[shift:] + k_up[:shift]
        map_low = dict(zip(k_low, v_low))
        map_up = dict(zip(k_up, v_up))
        return {**map_low, **map_up}

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        mapping = self.build_shift_dict(shift)
        shifted_text = ''
        for i in self.message_text:
            if i in mapping:
                shifted_text += mapping[i]
            else:
                shifted_text += i
        return shifted_text


print(string.ascii_lowercase + string.ascii_uppercase)
print(Message('Xie').apply_shift(5))

